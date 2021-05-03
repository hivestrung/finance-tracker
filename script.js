var dom1 = document.getElementById("container1");
var myChart1 = echarts.init(dom1);
var app1 = {};
var seriesdata1 = []
for (var i = 0; i < category_stats[0].length; i++) {
    var category = category_stats[0][i][0];
    var total = category_stats[0][i][1];
    var average = category_stats[0][i][2];
    if (category.localeCompare("deposit")) {
            seriesdata1.push({
            value: total, 
            name:category, 
            label: {show: true}
        })
    }
}
console.log(seriesdata1)
var option;
option = {
    title: {
        text: 'expenses per category',
        subtext: 'example',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        showContent: false
    },
    toolbox: {

    },
    legend: {
        data: ["automotive","clothing","deposit","education","electronics","entertainment","e transfers","fine","fee","gas","general merchandise","government","groceries","healthcare","home improvement","finance","loans","mobile","other","personal care","restaurants","travel","utilities","withdrawl"],
        left: 'left',                
        orient: 'vertical'
    },
    series: [
        {
            name: 'categories',
            type: 'pie',
            radius: '30%',
            center: ['50%', '25%'],
            data: seriesdata1,
            emphasis: {focus: 'data'}
        }
    ]
};

if (option && typeof option === 'object') {
    myChart1.setOption(option);
}

var dom2 = document.getElementById("container2");
var myChart2 = echarts.init(dom2);
var app2 = {};
var option2;
var seriesdata2 = [];
var legend = [];
for(var i = start_year; i <= end_year; i++) {
    legend.push('' + i)
}
console.log(years);
option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // Use axis to trigger tooltip
            type: 'shadow'        // 'shadow' as default; can also be 'line' or 'shadow'
        }
    },
    legend: {
        data: legend
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value'
    },
    yAxis: {
        type: 'category',
        data: ['withdrawl', 'utilities', 'travel', 'restaurants', 'personal care', 'other', 'mobile', 'loans', 'finance', 'home improvement', 'healthcare', 'groceries', 'government', 'general merchandise', 'gas', 'fee', 'fine', 'e transfers', 'entertainment', 'electronics', 'education', 'deposit', 'clothing', 'automotive']
    },
    series: [
        {
            name: '2014',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [320, 302, 301, 334, 390, 330, 320]
        },
        {
            name: '2015',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: '2016',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: '2017',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [150, 212, 201, 154, 190, 330, 410]
        },
        {
            name: '2018',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [820, 832, 901, 934, 1290, 1330, 1320]
        }
    ]
};

if (option && typeof option === 'object') {
    myChart2.setOption(option);
}