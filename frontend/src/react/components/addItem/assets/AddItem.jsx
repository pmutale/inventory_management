import React from "react";
import AddItemModal from "./snippets/AddItemModal";
import store from "../redux/store";

export default class AddItem extends React.Component {
	constructor(props) {
		super(props);
		this.state = {

		};

	}

	render() {
		const { url, item, pageInstance, category, category_id } = this.props;
		return (
			<span>
        <AddItemModal category={category}
                      url={url}
                      item={item}
                      category_id={category_id}
                      pageInstance={pageInstance}
                      store={store}/>
			</span>
		)
	}

}
