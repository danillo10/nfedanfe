const axios = require('axios');
const fs = require('fs');

// URL do endpoint
const url = 'https://consultadanfe.com/CDanfe/chave/';

// Configuração do payload com a chave e o token reCAPTCHA
const data = new URLSearchParams();
data.append('chave', '31240852279212000153550010000010261897822760');  // substitua pela chave do seu arquivo
data.append('g-recaptcha-response', '03AFcWeA7-Bbu35C0nkb65yIe32gsw2W46KyPzN6SZS4vN4Z9U83wheArolCG5i93j52p6TAo53tTM3r3AtCEIYZ_c2YVcUy9ivVHqwdzVGnYRo79ECAgNxsjaGG3JuwAHphlqAvbhwnncnFsWxMquKZ0NqlhXPMEZpFbPssvpmVksIBsjD75uuONUs5A2g9z2gSYelew7_s9Up6AsBjQJIMSREEJfiW6orJg3FbRJxDTMF1m8Hjs7QArSNMeJ8MIcogUvCTxwbFTo1_KCL2t_5JtBYTxghvpID0mF0pQPX8YVNoMBjaVOSE88HY9MuxIpdOOFWCYKvXNt6I9Fv_rvXSYzysj6oYIrFaPq5BQJxjrz8aMQETsJPfpcmWSQCJDIfw1vd_7In9y_uAZZlgBFlgAm8tiu3w5N3VV5JghzZWPHB0GjgmCti6efqCZ8NzJtdU1SBq1Kie7GnneoWrzqlCWjOm9dPMFp36fHSt2uMYgonjBY5HQt5sin_U87HrPAW6wHEjZF-brhTerI74JsgmJ2aB_U1258WYKHt-Ggew2urn7C5p4BZZiOkDXRjCLQuxM_-Quu8I54Agj53GuoP1zmLbQujkh9UrY7_sIdVRnkRttwGcgT4tKLRZ2uxkQcyFyGFblSPJx6_-akHE1u9Q5zqhVhwuLcQniRsfFwulX5soznmaGeECA26An3SluJ4vO3EBcHTgwVrn7Cm5FmP-JeNYmmgg2we7icjzS26ecK8j3PACRB-KIykOY0_sLR6-_WueZDmdyzLjchg48hfkpnPyuEb2a_EX2C3c_irURVScmxaBd3DhDrRz2PiRt5QR11lm-DNdw0zu_-g1hiAiDneolBEgTR8ONGJnlEd5yvpDLD1s_wRoOZAgJQQ3UMZCx0yhuBO1Pn68Fa-vlO7oQOcEemuCgPSQtvjRz0fumnRtEsBXgaXQM');

// Configuração dos cabeçalhos
const headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

// Função para enviar a requisição e salvar a resposta em um arquivo HTML
async function consultarDanfe() {
    try {
        const response = await axios.post(url, data, { headers });

        if (response.status === 200) {
            console.log("DANFE retornado com sucesso.");

            // Converte o response para string e grava em um arquivo HTML
            const responseHtml = JSON.stringify(response.data, null, 2);
            fs.writeFileSync('resposta.html', responseHtml);
            console.log('Resposta salva como resposta.html');
        } else {
            console.error('Erro ao consultar o DANFE:', response.statusText);
        }
    } catch (error) {
        console.error('Erro na requisição:', error.message);
    }
}

// Executa a função para realizar a consulta
consultarDanfe();
