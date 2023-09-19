//VALIDACIÓN DE FORMULARIO
function validarForm(){
          
    let isCorrect=true;
    
    if(document.getElementById("InputName").value.length < 2 ){
      isCorrect = false;
      
    }
     
    if(document.getElementById("InputAsunto").value.length < 2 ){
      
      isCorrect = false;
      
    }
  
    if(document.getElementById("InputEmail1").value.length < 5 ){
        isCorrect = false;
    }
        if (isCorrect){
  
            alert("Los datos fueron enviados.");
           
            return true;
  
            } else {
              alert("Por favor, revise los datos ingresados!!");
              return false
  
            }
          
        return isCorrect;
      
  }
  
  function limpiarInput(){
  
    document.getElementById("InputName").value = "";
    document.getElementById("InputDNI").value = "";
    document.getElementById("InputEmail1").value = "";
    document.getElementById("InputAsunto").value = "";
    document.getElementById("InputComentario").value = "";
    
  }
  