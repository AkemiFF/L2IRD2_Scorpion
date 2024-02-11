function changeConseils() {
  var probleme = document.getElementById("probleme").value;
  var conseilsElement = document.getElementById("conseils");
  if (probleme === "Administratrion") {
    conseilsElement.innerHTML = `
      <h2>Administratrion :</h2>

      <p>
        <ul>
          <li>Vérifiez les conditions de circulation avant de partir.</li>
          <li>Utilisez les transports en commun ou le covoiturage.</li>
          <li>Empruntez des itinéraires secondaires si possible.</li>
          <li>Soyez patient et respectez les autres conducteurs.</li>
        </ul>
      </p>
      
    `;
  } else if (probleme === "electricite") {
    conseilsElement.innerHTML = `
      <h2>Conseils pour les problèmes d'électricité:</h2>

      <p>
          <ul>
            <li>  Vérifiez si votre disjoncteur a sauté.  </li>
            <li>  Contactez votre fournisseur d'électricité.  </li>
            <li>  Utilisez des générateurs ou des batteries de secours si possible. </li>
            <li>  Soyez prudent et évitez d'utiliser des appareils électriques endommagés.  </li>
          </ul>
      </p>

    `;
  } else {
    conseilsElement.innerHTML = `
      <h2>Veuillez choisir entre: </h2>

      <p> <li>  Circulation et Eléctricité </li> </p>
      
    `;
  }
}

document.getElementById("probleme").addEventListener("change", changeConseils);