import express from 'express';
import { config as configDotenv } from 'dotenv';
import cors from 'cors';
import router from "./routes/authRoutes.js";
import mongoose from 'mongoose';

configDotenv();

// Updated connection URI and added options
mongoose.connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('Connected to database'))
.catch((err) => console.error('Database not connected', err));

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 4000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cors());  // Added CORS middleware

app.use("/", router);

// Start server
app.listen(PORT, () => {
    console.log(`App running on port ${PORT}`);
});
