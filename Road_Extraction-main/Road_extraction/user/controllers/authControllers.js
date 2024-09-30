import express from "express";
import userModel from "../models/user.js";
import bcrypt from "bcryptjs"; // Make sure to install bcryptjs

// Test route
const test = (req, res) => {
    res.json("test successful");
}

// Register a new user
const registerUser = async (req, res) => {
    try {
        const { username, password } = req.body;

        // Validate username
        if (!username) {
            return res.status(400).json({
                error: 'Username is required',
            });
        }

        // Validate password
        if (!password || password.length < 6) {
            return res.status(400).json({
                error: 'Password is required and should be at least 6 characters long',
            });
        }

        // Check if the username already exists
        const exists = await userModel.findOne({ username });
        if (exists) {
            return res.status(400).json({
                error: 'Username already exists',
            });
        }

        // Hash the password before saving
        const hashedPassword = await bcrypt.hash(password, 10);

        // Create the user
        const user = await userModel.create({
            username,
            password: hashedPassword,
        });

        // Return the user object as a response
        return res.status(201).json(user);
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            error: 'Server error. Please try again later.',
        });
    }
}

// Login a user
const loginUser = async (req, res) => {
    try {
        const { username, password } = req.body;

        // Validate username and password
        if (!username || !password) {
            return res.status(400).json({
                error: 'Username and password are required',
            });
        }

        // Find the user
        const user = await userModel.findOne({ username });
        if (!user) {
            return res.status(400).json({
                error: 'Invalid username or password',
            });
        }

        // Check if the password matches
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({
                error: 'Invalid username or password',
            });
        }

        // Login successful
        return res.status(200).json({ message: 'Login successful', user });
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            error: 'Server error. Please try again later.',
        });
    }
}

// Get all users
const getUsers = async (req, res) => {
    try {
        const users = await userModel.find({});
        return res.status(200).json(users);
    } catch (error) {
        console.error(error);
        return res.status(500).json({
            error: 'Failed to fetch users. Please try again later.',
        });
    }
}

export { test, registerUser, loginUser, getUsers }; // Make sure to export the new function



