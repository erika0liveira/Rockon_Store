const botao_login = $("button#login")
const campo_email = $("input#email")
const campo_senha = $("input#senha")

$(() => {
    checkCamposObrigatorios()
})

campo_email.on("input", () => {
    checkCamposObrigatorios()
})

campo_senha.on("input", () => {
    checkCamposObrigatorios()
})

function checkCamposObrigatorios(){
    const campos_vazios_login = (campo_email.val().length == 0 || campo_senha.val().length == 0)

    botao_login.toggleClass("desabilitado", campos_vazios_login)
    botao_login.toggleClass("habilitado", !campos_vazios_login)
    botao_login.attr("disabled", campos_vazios_login)
}
