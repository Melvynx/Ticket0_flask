function onEditPriority(id) {
  $(`#priority-name-${id}`).attr("disabled", false);
  $(`#priority-description-${id}`).attr("disabled", false);
  $(`#priority-level-${id}`).attr("disabled", false);
  $(`#priority-edit-${id}`).hide();
  $(`#priority-save-${id}`).show();
  $(`#priority-save-${id}`).show();
}

function onSavepPriority(id) {
  $(`#priority-name-${id}`).attr("disabled", true);
  $(`#priority-description-${id}`).attr("disabled", true);
  $(`#priority-level-${id}`).attr("disabled", true);
  $(`#priority-edit-${id}`).show();
  $(`#priority-save-${id}`).hide();
  $(`#priority-save-${id}`).hide();
}
