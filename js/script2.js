function addError(field) {
  if (field.previousElementSibling &&
    field.previousElementSibling.className === 'error') {
    // error message already showing
    return;
  }
  const error = document.createElement('div');
  error.innerHTML = '&#x26A1; '
    + field.dataset.errorMsg;
  error.className = 'error';
  field.parentNode.insertBefore(error, field);
}

function removeError(field) {
  if (field.previousElementSibling &&
    field.previousElementSibling.className === 'error') {
    field.previousElementSibling.remove();
  }
}

function checkField(field) {
  if (!field.checkValidity()) {
    addError(field);
  } else {
    removeError(field);
  }
}

function checkSelect(field) {
  if ( field.selectedIndex === 0 ) {
    field.setCustomValidity('Invalid');
    addError(field);
  } else {
    field.setCustomValidity('');
    removeError(field);
  }
}

window.addEventListener('load', function(e) {
  const form  = document.getElementById('subs_form');

  const email = form.email;
  email.dataset.errorMsg = 'Invalid Email';
  
  const name = form.name;
  name.dataset.errorMsg = 'name must be 8 to 25 characters.';

  const choice = form.choice;
  choice.dataset.errorMsg = 'Please select a training programme.';
  
  
  
  name.addEventListener("input", function(e) {
    checkField(name);
  });
  
  email.addEventListener("input", function(e) {
    checkField(email);
  });
  
  

  choice.addEventListener("change", function(e) {
    checkSelect(choice);
  });

 

  form.addEventListener("submit", function(e) {
    // Check errors
    checkField(name);
    checkField(email);
    checkSelect(choice);
    

    // If form is invalid, prevent submission
    if (!form.checkValidity()) {
      e.preventDefault();
      alert('Please fix form errors.');
    }
  });

});
