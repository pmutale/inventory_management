import ReactDOM from "react-dom";
import React from "react";
import {hot} from "react-hot-loader";
import AddItem from "./assets/AddItem";
import { Provider } from "react-redux";
import store from "./redux/store";

const inputElement = document.getElementById('add_item');

ReactDOM.render(
	<Provider store={store} >
		<AddItem url={inputElement.dataset.url}
		         item={inputElement.dataset.item}
		         category={inputElement.dataset.category}
		         pageInstance={inputElement.dataset.pageInstance} />
	</Provider>, inputElement);



export default hot(module)(AddItem)

