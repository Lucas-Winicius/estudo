import { Router } from "express";
const router = new Router();
import homeController from '../contollers/Home'

router.get("/", homeController.index);

export default router;
