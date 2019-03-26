import { combineReducers } from "redux";
import visibilityFilter from "./visibilityFilter";
import product from "./product";

export default combineReducers({ product, visibilityFilter });
