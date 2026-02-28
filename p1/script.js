const notes = [];

/**
 * Přidání poznámky k textu
 */
function addNote(textId) {
  const content = prompt("Napiš poznámku:");
  if (!content) return;

  const note = {
    id: crypto.randomUUID(),
    textId: textId,
    content: content,
  };

  notes.push(note);
  renderNotes();
}

/**
 * Smazání textu (poznámka zůstává)
 */
function deleteText(textId) {
  const textEl = document.getElementById(textId);
  if (textEl) {
    textEl.remove();
  }
  renderNotes();
}

/**
 * Vykreslení poznámek
 */
function renderNotes() {
  const container = document.getElementById("notes-list");
  container.innerHTML = "";

  notes.forEach((note) => {
    const exists = document.getElementById(note.textId);

    const div = document.createElement("div");
    div.className = "note" + (exists ? "" : " orphan");

    div.innerHTML = `
      <strong>${exists ? "Poznámka k textu" : "Nepřiřazená poznámka"}</strong>
      <p>${note.content}</p>
    `;

    container.appendChild(div);
  });
}
