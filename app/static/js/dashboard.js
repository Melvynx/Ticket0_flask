function onEnd(event) {
  stateID = event.to.dataset.stateid;
  tiqetID = event.item.dataset.tiqetid;
  editTiqetState(stateID, tiqetID, (state) => {
    console.log(state);
  });
}

// edit tiqet api
function editTiqetState(idState, idTiqet, callback) {
  const newState = { tiqet: { state: idState } };
  const newStateJson = JSON.stringify(newState);

  fetch(`${API_URL}/tiqet/${idTiqet}/state`, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: newStateJson,
  }).then((reponse) => {
    if (reponse.status !== 200) {
      console.warn("Tiqeto api has problem.");
      callback && callback({ state: "danger", status: "error server" });
      return;
    }

    reponse.json().then((state) => {
      callback && callback(state);
    });
  });
}
