import { VISIBILITY_FILTERS } from "../constants";

export const getFormState = store => store.todos;

export const getFormList = store =>
  getFormState(store) ? getFormState(store).allIds : [];

export const getFormById = (store, id) =>
  getFormState(store) ? { ...getFormState(store).byIds[id], id } : {};

export const getForm = store =>
  getFormList(store).map(id => getFormById(store, id));

export const getFormByVisibilityFilter = (store, visibilityFilter) => {
  const allForms = getForm(store);
  switch (visibilityFilter) {
    case VISIBILITY_FILTERS.AUDIO_VISUAL:
      return allForms.filter(todo => todo.completed);
    case VISIBILITY_FILTERS.BINDERS_AND_CLIPBOARDS:
      return allForms.filter(todo => !todo.completed);
    case VISIBILITY_FILTERS.COMPUTERS:
    default:
      return allForms;
  }
};
