# encoding=utf8  
# coding=UTF-8

TOKEN_SS = '##NUMSS##'
TOKEN_DATA = '##DATA##'
TOKEN_SITUACAO = '##SITSS##'
TOKEN_JS_DATA =  '##JSDATA##'
TOKEN_JS_DATASETS = '##JSDATASETS##'
TOKEN_JS_COR = "##JSCOR##"

#CONSULTA_ALM = "https://alm.serpro/ccm/web/projects/Neg%C3%B3cio%20(Solicita%C3%A7%C3%A3o%20de%20Servi%C3%A7o)#action=com.ibm.team.workitem.runSavedQuery&id=_FujlYGN3EeiWRMEsDorrSQ"
CONSULTA_ALM = "https://alm.serpro/ccm/web/projects/Neg%C3%B3cio%20(Solicita%C3%A7%C3%A3o%20de%20Servi%C3%A7o)#action=com.ibm.team.workitem.runSavedQuery&id=_4gKuIG_PEeiWTcEsDorrSQ"
ARQ_LOGIN_ALM = '/home/00937325465/familiai/login_alm/login'

SIT_SUSPENSA = "Suspensa"
CAMINHO_XML_SS = "/home/00937325465/familiai/rastreiai/xml/"
CAMINHO_HTML = "/home/00937325465/familiai/rastreiai/html/"
URL_LOGIN = 'https://alm.serpro/ccm/auth/j_security_check'
LISTA_SS = [1535442]
URL_HIST = 'https://alm.serpro/ccm/service/com.ibm.team.workitem.common.internal.rest.IWorkItemRestService/workItemDTO2?id=' + TOKEN_SS + '&includeAttributes=false&includeLinks=false&includeApprovals=false&includeHistory=true&includeLinkHistory=false'
TAG_MUDANCA_ESTADO = '<td class="HistoryColumn0">Status'
TAG_SEP_MUDANCA_ESTADO = '&nbsp;&nbsp;&rarr;&nbsp;&nbsp;'
SITUACOES = {'Aberta':0,\
            'Em Análise':1,\
            'Em Estimativa':2,\
            'Aguardando Autorização de Estimativa':3,\
            'Estimativa Aprovada':4,\
            'Em Atendimento':5,\
            'Entregue':6,\
            'Em Homologação':7,\
            'Homologação Aceita':8,\
            'Homologação Recusada':9,\
            'Homologada e Aguardando Implantação':10,\
            'Em Implantação':11,\
            'Suspensa':-1}

CONTEUDO_JS_DATA = """
{
                x: new Date(\"""" + TOKEN_DATA +  """\"),
                y: """ + TOKEN_SITUACAO + """ 
              },
"""

CONTEUDO_JS_DATASETS = """
    {label: '""" + TOKEN_SS + """',          
          data: [""" + TOKEN_JS_DATA + """             
          ],
          borderColor: [
          '""" + TOKEN_JS_COR + """'
          ],
          steppedLine: true,
          fill: false,
          borderWidth: 2},
"""

CONTEUDO_JS = """
<head>
    <meta charset="UTF-8">
</head>
<body>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.bundle.js"></script>
<div class="container">
  <canvas id="examChart"></canvas>
</div>

<script>
    var options = {month: 'numeric', day: 'numeric', year:'numeric' };
    var ctx = document.getElementById("examChart").getContext("2d");
    var yLabels = {
            0:'Aberta',
            1:'Em Análise',
            2:'Em Estimativa',
            3:'Aguardando Autorização de Estimativa',
            4:'Estimativa Aprovada',
            5:'Em Atendimento',
            6:'Entregue',
            7:'Em Homologação',
            8:'Homologação Aceita',
            9:'Homologação Recusada',
            10:'Homologada e Aguardando Implantação',
            11:'Em Implantação'
        }
    var myChart = new Chart(ctx, {
      type: 'line',        
      data: {
        labels: [],
        datasets: [
          """ + TOKEN_JS_DATASETS + """
        ]
      },
      options: { 
        elements: {
          line: {
              tension: 0
          },              
        },
        scales: {
            yAxes: [{
                ticks: {                    
                    stepSize: 1,
                    min: -1,
                    callback: function(value, index, values) {
                        // for a value (tick) equals to 8
                        return yLabels[value];
                        // 'junior-dev' will be returned instead and displayed on your chart
                    }
                }
            }],
            xAxes: [{
                type: 'time'}],
        }
}
    });
</script>
"""
