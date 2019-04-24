# encoding=utf8  
# coding=UTF-8

TOKEN_SS = '##NUMSS##'
TOKEN_DATA = '##DATA##'
TOKEN_SITUACAO = '##SITSS##'
TOKEN_DATA =  '##JSDATA##'
TOKEN_DATASET = '##JSDATASET##'
TOKEN_COR = "##JSCOR##"
TOKEN_CONT = "##CONT##"
TOKEN_ARRAY_SS = "##ARRAYSS##"
TOKEN_ARRAY_PEN = "##ARRAYPEN##"
TOKEN_FUN_TODAS = "##FUNTODAS##"
TOKEN_FUN_ATIVAS = "##FUNATIVAS##"
TOKEN_FUN_SUSPENSAS = "##FUNSUSPENSAS##"
TOKEN_FUN_AGUARDANDO_CLI = "##FUNAGCLI##"
TOKEN_FUN_AGUARDANDO_DES = "##FUNAGDES##"
TOKEN_FUN = "##FUN##"
TOKEN_POINTSTYLE = "##POINTSTYLE##"
TOKEN_RADIUS = "##RADIUS##"
TOKEN_POINTBGCOLOR = "##POINTBGCOLOR##"
TOKEN_ARRAY_SS_ATIVAS = "##SSATIVAS##"
TOKEN_ARRAY_SS_SUSP = "##SSSUSP##"
TOKEN_ARRAY_SS_AC = "##AGCLI##"
TOKEN_ARRAY_SS_AD = "##AGDES##"

#CONSULTA_ALM = "https://alm.serpro/ccm/web/projects/Neg%C3%B3cio%20(Solicita%C3%A7%C3%A3o%20de%20Servi%C3%A7o)#action=com.ibm.team.workitem.runSavedQuery&id=_FujlYGN3EeiWRMEsDorrSQ"
CONSULTA_ALM = "https://alm.serpro/ccm/web/projects/Neg%C3%B3cio%20(Solicita%C3%A7%C3%A3o%20de%20Servi%C3%A7o)#action=com.ibm.team.workitem.runSavedQuery&id=_4gKuIG_PEeiWTcEsDorrSQ"
ARQ_LOGIN_ALM = '/home/00937325465/familiai/login_alm/login'

SIT_SUSPENSA = "Suspensa"

SG_AGUARDANDO_DES = "AD"
SG_AGUARDANDO_CLI = "AC"
#CAMINHO_XML_SS = "/home/00937325465/familiai/rastreiai/xml/"
CAMINHO_XML_SS = "./xml/"
#CAMINHO_HTML = "/home/00937325465/familiai/rastreiai/html/"
CAMINHO_HTML = "./html/"
URL_LOGIN = 'https://alm.serpro/ccm/auth/j_security_check'
LISTA_SS = [1535442]
URL_HIST = 'https://alm.serpro/ccm/service/com.ibm.team.workitem.common.internal.rest.IWorkItemRestService/workItemDTO2?id=' + TOKEN_SS + '&includeAttributes=false&includeLinks=false&includeApprovals=false&includeHistory=true&includeLinkHistory=false'
TAG_MUDANCA_ESTADO = '<td class="HistoryColumn0">Status'
TAG_AGUARDANDO_CLI = "Added:&#xA;&lt;br />&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;aguardando_urc"
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
            'Suspensa':-1,\
            'Aguardando Cliente':-2}

JS_DATA = "{x: new Date('" + TOKEN_DATA + "'), y: " + TOKEN_SITUACAO + " },"

JS_NM_ARRAY_SS = "array_ss"
JS_DEC_ARRAY_SS = "var " + JS_NM_ARRAY_SS + " = new Object();\n"
JS_ARRAY_SS = JS_NM_ARRAY_SS + "['" + TOKEN_SS + "'] = {label: '" + TOKEN_SS +"',\n" +\
                                                        "\tdata: [" + TOKEN_DATA+"],\n" +\
                                                        "\tborderColor: ['" + TOKEN_COR + "'],"+\
                                                        "\tsteppedLine: true, fill: false,"+\
                                                        "\tpointStyle: [" + TOKEN_POINTSTYLE +"],\n" +\
                                                        "\tradius: [" + TOKEN_RADIUS+"],\n" +\
                                                        "\tpointBackgroundColor: [" + TOKEN_POINTBGCOLOR + "]};\n"
JS_NM_ARRAY_PEN = "array_pen"
JS_DEC_ARRAY_PEN = "var " + JS_NM_ARRAY_PEN + " = new Object();\n"
JS_ARRAY_PEN = JS_NM_ARRAY_PEN + "['" + TOKEN_SS + "'] = {label: '" + TOKEN_SS +"',\n" +\
                                                        "\tdata: "+  JS_NM_ARRAY_SS +"['" + TOKEN_SS+"'].data,\n" +\
                                                        "\tborderColor: "+  JS_NM_ARRAY_SS +"['" + TOKEN_SS+"'].borderColor,\n" +\
                                                        "\tsteppedLine: true, fill: false,"+\
                                                        "\tpointStyle: [" + TOKEN_POINTSTYLE +"],\n" +\
                                                        "\tradius: [" + TOKEN_RADIUS+"],\n" +\
                                                        "\tpointBackgroundColor: [" + TOKEN_POINTBGCOLOR + "]};\n"


JS_NM_ARRAY_SS_ATIVAS = "array_ss_ativas"
JS_ARRAY_ATIVAS = JS_NM_ARRAY_SS_ATIVAS + " = [" + TOKEN_ARRAY_SS_ATIVAS + "];\n"

JS_NM_ARRAY_SS_SUSP = "array_ss_suspensas"
JS_ARRAY_SUSP = JS_NM_ARRAY_SS_SUSP + " = [" + TOKEN_ARRAY_SS_SUSP + "];\n"

JS_NM_ARRAY_SS_AC = "array_ss_aguardando_cli"
JS_ARRAY_AC = JS_NM_ARRAY_SS_AC + " = [" + TOKEN_ARRAY_SS_AC + "];\n"

JS_NM_ARRAY_SS_AD = "array_ss_aguardando_des"
JS_ARRAY_AD = JS_NM_ARRAY_SS_AD + " = [" + TOKEN_ARRAY_SS_AD + "];\n"


JS_FUN="""
    {
        myLineChart.data.datasets = [""" + TOKEN_DATASET +"""]
        myLineChart.update();
    }\n
"""


JS = """
<head>
    <meta charset="UTF-8">
</head>
<body>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.bundle.js"></script>
<div class="container">
  <canvas id="myChart"></canvas>
</div>

<script>
    var canvas = document.getElementById('myChart');""" +\
    JS_DEC_ARRAY_SS +\
    TOKEN_ARRAY_SS +\
    JS_DEC_ARRAY_PEN +\
    TOKEN_ARRAY_PEN +\
    JS_ARRAY_ATIVAS +\
    JS_ARRAY_SUSP +\
    JS_ARRAY_AC +\
    JS_ARRAY_AD + """
    
    var yLabels = {
            '-2':'Aguardando CLIENTE',
            '-1':'Suspensa',
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
    var option = {
        showLines: true,
        scales: {            
                xAxes: [{
                    type: 'time'}],
                yAxes: [{
                ticks: {                    
                    stepSize: 1,
                    min: -5,
                    callback: function(value, index, values) {
                        // for a value (tick) equals to 8
                        return yLabels[value];
                        // 'junior-dev' will be returned instead and displayed on your chart
                    }
                }
            }],
            }
    };

    var data = {    
        datasets: [{label: '', 
        	data: [{x: '', y: '' }] ,
        	borderColor: [''],
         }, ]
    };

    var myLineChart = Chart.Line(canvas,{
        data:data,
        options:option
    });
    

    function renderizar(ss){
            pend = document.getElementById("pend").checked
            if(pend){
            	dados = """ + JS_NM_ARRAY_PEN + """[ss];
            }else{
            	dados = """ + JS_NM_ARRAY_SS + """[ss];
            }
            
            myLineChart.data.datasets.push(dados);
            myLineChart.update();
    }

    function atualizar(){
    	 myLineChart.data.datasets = [];
         myLineChart.update();
         ativ = document.getElementById("ativ").checked;
         susp = document.getElementById("susp").checked;
    	 ac = document.getElementById("ac").checked;
         ad = document.getElementById("ad").checked;
         juncao = [];
         if(ativ && susp){
        	juncao = """+JS_NM_ARRAY_SS_ATIVAS+""".concat(array_ss_suspensas);
         } else if(ativ){
         	juncao = """+JS_NM_ARRAY_SS_ATIVAS+""";
         } else if(susp){
         	juncao = """+JS_NM_ARRAY_SS_SUSP+""";
         }
         comparador = juncao;
         if(ac && ad){
         	comparador = """ + JS_NM_ARRAY_SS_AC + """.concat(""" + JS_NM_ARRAY_SS_AD + """);
         } else if(ac){
         	comparador = """ + JS_NM_ARRAY_SS_AC + """;
         } else if(ad){
         	comparador = """ + JS_NM_ARRAY_SS_AD + """;
         } 
         
         interseccao = [];
         if(comparador.length && juncao.length){
         	interseccao = juncao.filter(value => -1 !== comparador.indexOf(value))
         } else if (comparador.length){
         	interseccao = comparador;
         } else if (juncao.length){
         	interseccao = juncao;
         }
         
         interseccao.forEach(renderizar);       
        
    }
    
</script>
<br>
<table><tr><td>
<input type="checkbox" id="ativ" onclick="atualizar()">Ativas<br>
<input type="checkbox" id="susp" onclick="atualizar()">Suspensas<br>
</td><td>
<input type="checkbox" id="ac" onclick="atualizar()">Aguardando Cliente<br>
<input type="checkbox" id="ad" onclick="atualizar()">Aguardando Des<br>
</td></tr><tr><td colspan=2>
<input type="checkbox" id="pend" onclick="atualizar()">Exibir Pendências<br>
</td></tr></table>

"""
