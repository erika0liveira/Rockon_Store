const incrementa = document.querySelector('#incrementa')
const decrementa = document.querySelector('#decrementa')
const quantidade = document.querySelector('#qtde')
const add_carrinho = document.querySelector('#adicionar-carrinho')

let qtde = Number(quantidade.value)

// REFATORAR ESSE CODIGO PORCO

incrementa.addEventListener('click', ()=>{
    qtde++
    quantidade.value = qtde
    checkQtde()
})

decrementa.addEventListener('click', ()=>{
    if(qtde - 1 >= 0){
        qtde--
        quantidade.value = qtde
    }
    checkQtde()
})

window.addEventListener('load', ()=>{
    checkQtde()
})

function checkQtde(){
    if(!(qtde > 0)){
        add_carrinho.classList.add('desabilitado')
        add_carrinho.disabled = true
    }else{
        add_carrinho.classList.remove('desabilitado')
        add_carrinho.disabled = false
    }
}




