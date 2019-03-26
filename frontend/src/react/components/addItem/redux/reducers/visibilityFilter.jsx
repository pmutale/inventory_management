import { FILTER_PRODUCT_FORM } from "../actionTypes";
import { VISIBILITY_FILTERS } from "../../constants";

const initialState = VISIBILITY_FILTERS.NONE;

const visibilityFilter = (state = initialState, action) => {
  switch (action.type) {
    case FILTER_PRODUCT_FORM: {
      return action.payload.filter;
    }
    default: {
      return state;
    }
  }
};

export default visibilityFilter;
