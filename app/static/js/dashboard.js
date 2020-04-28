function onEnd(event) {
  stateID = event.to.dataset.stateid;
  tiqetID = event.item.dataset.tiqetid;
  editTiqet(tiqetID, { fk_state: stateID });
}
