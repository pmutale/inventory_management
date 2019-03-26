import React from "react";
import { connect } from "react-redux";
import {VISIBILITY_FILTERS} from "../../constants";
import { setFilterProduct } from "../../redux/actions";

const VisibleForm = ({ activeFilter, setFilter }) => {
  return (
    <div className="visibility-filters">
      {Object.keys(VISIBILITY_FILTERS).map(filterKey => {
        const currentForm = VISIBILITY_FILTERS[filterKey];
        return (
          <span
            key={`visibility-filter-${currentForm}`}
            onClick={() => {
              setFilter(currentForm);
            }}
          >
            {currentForm}
          </span>
        );
      })}
    </div>
  );
};

const mapStateToProps = state => {
  return { activeFilter: state.visibilityFilter };
};

export default connect(
  mapStateToProps,
  { setFilterProduct }
)(VisibleForm);
