const campo_nome = $("input#nome")
const campo_sobrenome = $("input#sobrenome")
const campo_cpf = $("input#documento")
const campo_endereco = $("input#endereco")
const campo_numero = $("input#numero")
const campo_cep = $("input#cep")
const campo_email = $("input#email")
const campo_senha = $("input#senha")
const campo_senha2 = $("input#senha2")

let todos_campos = $(".info input")

const botao_cadastro = $("button#cadastro")

// REFAZER ESSE CÓDIGO PORCO

$(() => {
    checkCamposObrigatorios()
})

for(const campo of todos_campos){    
    campo.addEventListener('input', () => {
        checkCamposObrigatorios()
    })
}


function checkCamposObrigatorios(){

    campos_obrigatorios_cadastro = (
        campo_nome.val().length == 0 ||
        campo_sobrenome.val().length == 0 ||
        campo_cpf.val().length == 0 ||
        campo_endereco.val().length == 0 ||
        campo_numero.val().length == 0 ||
        campo_cep.val().length == 0 ||
        campo_email.val().length == 0 ||
        campo_senha.val().length == 0 ||
        campo_senha2.val().length == 0)

    botao_cadastro.toggleClass("desabilitado", campos_obrigatorios_cadastro)
    botao_cadastro.toggleClass("habilitado", !campos_obrigatorios_cadastro)
    botao_cadastro.attr("disabled", campos_obrigatorios_cadastro)
}
