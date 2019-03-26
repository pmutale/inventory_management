import {
  ADD_PRODUCT,
  ACTION_PRODUCT_SUCCESS,
  ACTION_PRODUCT_FAILURE,
  FILTER_PRODUCT_FORM,
  DELETE_PRODUCT,
  EDIT_PRODUCT }
  from "../actionTypes";

const initialState = {
  success: false,
  data: '',
  error: false,
  url: null
};

export default function(state = initialState, action) {
  switch (action.type) {
    case ADD_PRODUCT: {
      const { url } = action.payload;
      return {
        ...state,
        url: url,
        success: false

      }
    }

    case ACTION_PRODUCT_SUCCESS: {
      const { response } = action.payload;
      return {
          ...state,
          success: true,
          data: response
        }
    }

    case ACTION_PRODUCT_FAILURE: {
      const { error } = action.payload;
      return {
          ...state,
          data: error,
          error: true

        }
    }

    case EDIT_PRODUCT: {
      const { response } = action.payload;
      return {
          ...state,
          success: true,
          data: response
        }
    }

    case DELETE_PRODUCT: {
      const { response } = action.payload;
      return {
          ...state,
          success: true,
          data: response
        }
    }
    case FILTER_PRODUCT_FORM: {
      const { response } = action.payload;
      return {
          ...state,
          success: true,
          data: response
        }
    }
    default:
      return state;
  }
}
