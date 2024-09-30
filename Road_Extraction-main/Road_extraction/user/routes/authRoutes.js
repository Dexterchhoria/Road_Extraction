import express from "express";
import cors from "cors";
import { test, registerUser,loginUser, getUsers } from "../controllers/authControllers.js";

const router = express.Router();
router.use(
    cors(
        {
            credentials : true,
            origin : "http://localhost:3000"
        }
    )
);

router.get("/", test);
router.post('/register', registerUser);
router.get('/register', getUsers);
router.post('/login', loginUser);

export default router