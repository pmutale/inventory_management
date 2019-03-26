import {
	ADD_PRODUCT,
	ACTION_PRODUCT_FAILURE,
	DELETE_PRODUCT,
	EDIT_PRODUCT,
	FILTER_PRODUCT_FORM,
	ACTION_PRODUCT_SUCCESS
} from "./actionTypes";
import Cookies from "js-cookie";


const actionProductSuccess = (response) => ({
	type: ACTION_PRODUCT_SUCCESS,
	payload: {
		response,
	}
});

const actionProductFailure = (error) => ({
	type: ACTION_PRODUCT_FAILURE,
	payload: {
		error
	}
});

const addingProduct = (url) => ({
	type: ADD_PRODUCT,
	payload: {
		url
	}
});

export const editProduct = id => ({
	type: EDIT_PRODUCT,
	payload: { id }
});

export const deleteProduct = id => ({
	type: DELETE_PRODUCT,
	payload: { id }
});

export const setFilterProduct = filter => ({ type: FILTER_PRODUCT_FORM, payload: { filter } });


export const addProduct = (url, content) => {
	return (dispatch) => {
		dispatch(addingProduct(url));
		const postProduct = fetch( url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': Cookies.get('csrftoken'),
				'cache-control': 'no-cache',
			},
			cache: 'reload',
			body: JSON.stringify(
				content,
			),
		});

		return postProduct.then(
			response => {
				response.ok ?
					response.json().then(data => dispatch(actionProductSuccess(data))):
					response.json().then(data => dispatch(actionProductFailure(data)))
			}
		).catch(error => dispatch(actionProductFailure(error)))
	};


}


