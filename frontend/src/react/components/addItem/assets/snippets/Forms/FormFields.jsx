import React from "react";
import { Form, Icon, Grid, Select, Dropdown } from "semantic-ui-react";
import APISelectField from "../../../../helpers/APISelectField";
import { COUNTRY_OPTIONS } from "../../../../helpers/countriesData";

const errorPresence = (props, fieldName) => {
  return props.derivedResponse && !props.derivedResponse.success && Object.keys(props.derivedResponse.data).includes(fieldName);
};

const FormFields = (props) => {
  return (
    <Form>
      {
        Object.values(props.fields).map((field, key) => {
          return (
            ["description", "extras"].includes(field.name) ?
              <Form.TextArea placeholder={field.placeholder}
                error={errorPresence(props, field.name)}
                name={field.name}
                onChange={props.handleChange}
                value={field.value}
                key={key}
              /> :
              ["country_of_origin"].includes(field.name) ?
                <Form.Select
                  fluid
                  placeholder={field.placeholder}
                  value={field.value}
                  name={field.name}
                  search
                  error={errorPresence(props, field.name)}
                  selection
                  selectOnBlur={false}
                  options={COUNTRY_OPTIONS}
                  onChange={props.handleChange}
                /> :
                ["kind", "brand", "screen_type", "mounting_method" ].includes(field.name) ?

                  <Grid id={"selectKindBrand"}>
                    <Grid.Column width={15}>
                      <APISelectField
                        key={key}
                        onChange={props.handleChange}
                        name={field.name}
                        value={field.value}
                        fluid
                        placeholder={field.placeholder}
                        url={"/stock/audio_visual/" + field.name + ""}
                      /></Grid.Column>
                    <Grid.Column width={1}>
                      <div id={field.name}>
                        <a href={"#"}>
                          <Icon size={"big"} color={"purple"} name={"plus circle"}> </Icon>
                        </a>
                      </div>
                    </Grid.Column>
                  </Grid> :
                  <Form.Input icon={field.name === "serial_number" ? "barcode" : field.icon}
                    iconPosition={"left"}
                    type={field.name === "purchase_date" ? "date" : "text"}
                    value={field.value}
                    placeholder={field.placeholder}
                    error={errorPresence(props, field.name)}
                    name={field.name}
                    key={key}
                    onChange={props.handleChange}
                  />
          );
        }
        )
      }

    </Form>
  );
};

export default FormFields;
