import React, {Component} from "react";
import {Button, Modal} from "semantic-ui-react";
import AddAudioVisual from "./Forms/AddAudioVisual";
import {addProduct} from "../../redux/actions";
import AddKind from "./Forms/AddKind";
import AddBrand from "./Forms/AddBrand";
import { trans } from "../../../helpers/globalsFuncs.";

class AddItemModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
      category: {name: "", id: ""},
      postDataProduct: {},
      derivedResponse: null,
      kind: {
        add: false
      },
      brand: {
        add: false
      },
      formInstance: {
        name: "audio_visual" // Default Form Instance
      }

    };
    this.closeConfigShow = this.closeConfigShow.bind(this);
    this.handlePostData = this.handlePostData.bind(this);
    this.handleGetCurrentState = this.handleGetCurrentState.bind(this);
    this.close = this.close.bind(this);
    this.back = this.back.bind(this);
    this.addKind = this.addKind.bind(this);
    this.addBrand = this.addBrand.bind(this);
  }

  componentDidMount() {

  }

  closeConfigShow(el) {
    const category = {
      name: el.getAttribute("data-item"),
      id: el.getAttribute("data-id")
    };
    this.setState({ open: true, category: category});
  }

  back() {
    this.setState({
	    kind: {
	    	add: false
	    },
	    brand: {
	    	add: false
	    },
      derivedResponse: null,
      postDataProduct: {},
      formInstance: {
	      name: "audio_visual" // Maintaining the default instance on state callBack()
      }
    });
  }

  close() {
    this.setState({
      open: false,
      derivedResponse: null,
      postDataProduct: {} ,
      category: {},
      kind: {},
      brand: {}
    });
  }

  handlePostData(data) {
    data["category"] =  parseInt(this.state.category.id);
    data["country_of_origin"] = [data["country_of_origin"], ];
    this.setState({ postDataProduct: data });
  }

  addKind(start) {
    const { kind, formInstance } = this.state;
    if (start) {
      kind.add = true;
      formInstance.name = "kind";
      this.setState(kind);
    }
  }

  addBrand(start) {
    const { brand, formInstance } = this.state;
    if (start) {
      brand.add = true;
      formInstance.name = "brand";
      this.setState(brand);
    }
  }

  handleGetCurrentState(){
    setTimeout(() => {
      const currentState = this.props.store.getState();
      const currentStateInstance = currentState.product;
      currentStateInstance["instance"] = this.state.formInstance.name;
      this.setState({ derivedResponse: currentStateInstance });
    },500);
  }

  render() {
    const { open, postDataProduct, derivedResponse, category, kind, brand } = this.state;
    const { url, store, pageInstance } = this.props;
    const addItemSelector = document.querySelectorAll("#addItemModalPoint");

    const addForms = {
      ["audiovisual-equipment"]: <AddAudioVisual addBrand={this.addBrand}
        addKind={this.addKind}
        handlePostData={this.handlePostData}
        derivedResponse={derivedResponse}/>,
    };

    const currentUrl = kind.add ?
      url + trans("kind/"): brand.add ? url + trans("brand/") : url;
    const currentHeader = kind.add ?
      category.name + trans(" Kind"): brand.add ? category.name + trans(" Brand") : category.name;


    return (
      <div id={"addItemModal"}>
        {addItemSelector.forEach((el) => el.onclick = () => this.closeConfigShow(el))}
        <Modal id={"addItemModal"}
          open={open}
          closeOnEscape={false}
          closeOnDimmerClick={false}
          onClose={this.close}>
          <Modal.Header>Add {currentHeader} </Modal.Header>
          <Modal.Content>
            {
              brand.add ?
                <AddBrand handlePostData={this.handlePostData}
                  derivedResponse={derivedResponse}/>:
                kind.add ?
                  <AddKind handlePostData={this.handlePostData}
                    derivedResponse={derivedResponse}/> :
                  addForms[pageInstance]
            }
          </Modal.Content>
          <Modal.Actions>
            <Button onClick={this.close} negative>Cancel</Button>
            <Button onClick={this.back} disabled={!kind.add && !brand.add } negative>Back</Button>
            <Button
              disabled={derivedResponse && derivedResponse.success}
              onClick={() => (store.dispatch(addProduct(currentUrl, postDataProduct)), this.handleGetCurrentState())}
              positive
              labelPosition="right"
              icon="checkmark"
              content="Submit"
            />
          </Modal.Actions>
        </Modal>
      </div>
    );
  }
}

export default AddItemModal;
