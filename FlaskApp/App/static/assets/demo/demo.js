type = ['primary', 'info', 'success', 'warning', 'danger'];

demo = {
  initPickColor: function() {
    $('.pick-class-label').click(function() {
      var new_class = $(this).attr('new-class');
      var old_class = $('#display-buttons').attr('data-class');
      var display_div = $('#display-buttons');
      if (display_div.length) {
        var display_buttons = display_div.find('.btn');
        display_buttons.removeClass(old_class);
        display_buttons.addClass(new_class);
        display_div.attr('data-class', new_class);
      }
    });
  },

  initDocChart: function() {
    chartColor = "#FFFFFF";

    // General configuration for the charts with Line gradientStroke
    gradientChartOptionsConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      tooltips: {
        bodySpacing: 4,
        mode: "nearest",
        intersect: 0,
        position: "nearest",
        xPadding: 10,
        yPadding: 10,
        caretPadding: 10
      },
      responsive: true,
      scales: {
        yAxes: [{
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        }],
        xAxes: [{
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        }]
      },
      layout: {
        padding: {
          left: 0,
          right: 0,
          top: 15,
          bottom: 15
        }
      }
    };

    ctx = document.getElementById('lineChartExample').getContext("2d");

    gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
    gradientStroke.addColorStop(0, '#80b6f4');
    gradientStroke.addColorStop(1, chartColor);

    gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
    gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
    gradientFill.addColorStop(1, "rgba(249, 99, 59, 0.40)");

    myChart = new Chart(ctx, {
      type: 'line',
      responsive: true,
      data: {
        labels: ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun", "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"],
        datasets: [{
          label: "Active Users",
          borderColor: "#f96332",
          pointBorderColor: "#FFF",
          pointBackgroundColor: "#f96332",
          pointBorderWidth: 2,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 1,
          pointRadius: 4,
          fill: true,
          backgroundColor: gradientFill,
          borderWidth: 2,
          data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 630]
        }]
      },
      options: gradientChartOptionsConfiguration
    });
  },

  initDashboardPageCharts: function() {

    gradientChartOptionsConfigurationWithTooltipBlue = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#2380f7"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#2380f7"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipOrange = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 110,
            padding: 20,
            fontColor: "#ff8a76"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(220,53,69,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#ff8a76"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipGreen = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(0,242,195,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };


    gradientBarChartConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 120,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };

    var ctx = document.getElementById("chartLinePurple").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

    var data = {
      labels: ['LEPL1402', 'LSINF1101-Python', 'LSINF1252'],
      datasets: [{
        label: "Nombre de soumissions",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#d048b6',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#d048b6',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#d048b6',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [306140, 493620, 85563],
      }]
    };

    var myChart = new Chart(ctx, {
      type: 'pie',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipPurple
    });


    var ctxGreen = document.getElementById("chartLineGreen").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(66,134,121,0.15)');
    gradientStroke.addColorStop(0.4, 'rgba(66,134,121,0.0)'); //green colors
    gradientStroke.addColorStop(0, 'rgba(66,134,121,0)'); //green colors

    var data = {
      labels: ['OCT 2019', 'NOV 2019', 'DÉC 2019', 'JAN 2020'],
      datasets: [{
        label: "Nombre de soumissions",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#00d6b4',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#00d6b4',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#00d6b4',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: [193854, 84102, 24468, 582899],
      }]
    };

    var myChart = new Chart(ctxGreen, {
      type: 'line',
      data: data,
      options: gradientChartOptionsConfigurationWithTooltipGreen

    });



    var chart_labels = ['ASCIIDecoder', 'AbstractClass', 'AccessModifiers', 'Array2D', 'BlackBox', 'BoundedBuffer', 'BubbleSortInvariant', 'Casting', 'CircularLL', 'CodeAccuracy', 'CodeAccuracy2', 'CommonErrors', 'ComparatorAndCollections', 'ComparatorvsComparable', 'ComplexityArraySearch', 'ComplexityMCQ1', 'ComplexitySpaceMCQ', 'Coverage', 'CyclicBarrier', 'FList', 'FListMergeSort', 'FTree', 'Factory', 'Fibonacci', 'Future', 'Generics', 'Generics2', 'Generics3', 'HanoiTower', 'InfiniteStreams', 'Inheritance', 'Introduction', 'LambdaExpressioninJava', 'LearnException', 'MakeMistakeToUnderstandThem', 'MaximumSumSubarray', 'MergeSortImplementation', 'MidTermQuiz', 'MidTermQuizMCQ', 'MidTermQuizMCQ2', 'MyArrayList', 'Observer', 'Optional', 'ParallelelMergeSort', 'PostScript', 'ProducerConsumer', 'QueueWithStacks', 'SharedCounter', 'SieveOfEratosthenesImplementation', 'SieveOfEratosthenesMCQ', 'StackWithQueue', 'Streams', 'Streams2', 'StringUtils', 'ThreadsIntroduction', 'TreeCombineWith', 'TreeInorder', 'TreeSame', 'ValueOrReference', 'Visitor', 'VisitorBasic', 'complexityMCQ2', 'fail', 'valley'];
    var chart_data =
    [81, 83, 88, 77, 76, 81, 86, 89, 79, 43, 50, 89, 85, 67, 91, 86, 94, 70, 75, 76, 68, 83, 80, 86, 86, 82, 86, 78, 87, 57, 84, 79, 88, 88, 85, 71, 64, 59, 47, 50, 75, 88, 68, 65, 83, 78, 83, 91, 76, 93, 90, 79, 78, 77, 91, 83, 84, 82, 95, 82, 78, 88, 50, 74];


    var ctx = document.getElementById("chartBig1").getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors
    var config = {
      type: 'bar',
      data: {
        labels: chart_labels,
        datasets: [{
          label: "My First dataset",
          fill: true,
          backgroundColor: gradientStroke,
          borderColor: '#d346b1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: '#d346b1',
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: '#d346b1',
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: chart_data,
        }]
      },
      options: gradientChartOptionsConfigurationWithTooltipPurple
    };
    var myChartData = new Chart(ctx, config);
    $("#0").click(function() {
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });
    $("#1").click(function() {
      var chart_data = [70, 69, 50, 67, 65, 46, 17, 0, 80, 69, 61, 69, 0, 33, 54, 82, 0, 0, 0, 34, 0, 48, 70, 83, 78, 67, 81, 57, 40, 70, 62, 73, 74, 86, 88, 66, 84, 86, 63, 83, 85, 0, 76, 82, 25, 70, 0, 81, 62, 66, 58, 59, 83, 89, 70, 77, 75, 73, 62, 79, 75, 67, 0, 8, 76, 0, 70, 87, 77, 0, 20, 50, 74, 66, 70, 0, 0, 70, 52, 56, 84, 79, 66, 81, 82, 78, 72, 37, 72, 62, 33, 77, 73, 31, 51, 81, 70, 63, 56, 42, 36, 39, 31, 0, 0, 33, 41, 31, 26, 33, 66, 68, 0, 67, 0, 79, 62, 17, 51, 56, 51, 80, 77, 80, 53, 73, 56, 63, 0, 63, 50, 74, 77, 78, 70, 79, 80, 54, 78, 82, 80, 50, 68, 66, 70, 70, 51, 65, 0];
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = ['2degree', '2degree2', 'Acc', 'Ajoute', 'AmazonConstructor', 'AmazonPay', 'Append', 'Assistant', 'Average', 'Bath', 'BinarySearch', 'Carre', 'Compose', 'ComprehensionTranslation', 'Coordinates', 'Count', 'Count2', 'CountNested', 'Counters', 'DebtReminder', 'DeepConcat', 'DestroyAllEnnemies', 'DestroyAnEnnemy', 'DictCreation', 'DictCreationMax', 'DictKeyAccess', 'DiffCount', 'DoubleLink', 'DummyScript', 'Equals', 'Exam-ClientListUpdate', 'Exam-Enonce', 'Exam-LoadMatrix', 'Exam-PlusFrequent', 'Exam-RainFall', 'Exceptions', 'Factorial', 'Fibonacci', 'FileReading', 'FirstSum', 'FizzBuzz', 'Flatten', 'GCD', 'GD', 'GUI', 'Hello', 'HighOrder', 'Hogwarts-I', 'Hogwarts-II', 'Hogwarts-III', 'Hogwarts-IV', 'Hogwarts-V', 'Interests', 'Interval', 'LinkedList', 'LinkedListChildren', 'LinkedListEndRemove', 'LinkedListInit', 'LinkedListInsert', 'LinkedListRemove', 'LinkedListStr', 'LoadSaveGame', 'Map', 'Max', 'Median', 'Memoization', 'MergeList', 'Min', 'Morse', 'NCompose', 'NestParticipants', 'NestedMin', 'PairOpposite', 'PairOrdered', 'PairSame', 'Participants', 'PathModule', 'PatternExtraction-I', 'PatternExtraction-II', 'PatternExtraction-III', 'Polynomial', 'Prime', 'Primes', 'QBF01', 'QBF02', 'QBF03', 'QBF04', 'QBF05', 'QBF06', 'QBF07', 'QBF08', 'QBF09', 'QBF10', 'QBF10_2019', 'QBF11', 'Quetelet', 'REAL01', 'REAL02', 'REAL03', 'REAL04', 'REAL05', 'REAL06', 'REAL07', 'REAL07Review', 'REAL08', 'REAL09', 'REAL10', 'REAL10_2019', 'REAL11', 'REAL12', 'RSTTable', 'Recherche', 'RecursiveFactorial', 'RecursiveFibonacci', 'RecursiveSum', 'Remainder', 'SMSStore', 'SessTest_QCM', 'Session10_2019_QCM', 'Session10_QCM', 'Session11_QCM', 'Session1_QCM', 'Session2_QCM', 'Session3_QCM', 'Session4_QCM', 'Session5_QCM', 'Session6_QCM', 'Session7_QCM', 'Session8_QCM', 'Session9_QCM', 'Sieve', 'SimpleFactorial', 'SimpleMath', 'SimpleMax', 'Sort', 'SpeedingFine', 'StudentConstructor', 'StudentFileReading', 'StudentInit', 'Sum', 'SumToComplete', 'Testing', 'TextToDic', 'Ticket', 'Translator', 'Triangle', 'WrongIterations', 'ZooGame', 'unittest1'];
      myChartData.update();
    });

    $("#2").click(function() {
      var chart_data = [0, 90, 25, 88, 65, 43, 71, 79, 80, 97, 91, 72, 25, 90, 93, 90, 44, 92, 89, 95, 93, 86, 94, 37, 24, 18, 82, 93, 81, 95, 50, 95, 80, 14, 19, 35, 27, 66, 25, 14, 89, 91, 100, 28, 89, 83, 17, 90, 24, 14, 85, 37, 92, 92, 14, 91, 86, 29, 73, 84, 87, 94, 81, 87, 89, 85, 90, 90, 33, 25, 0, 33, 90, 87, 88, 85, 92, 93, 34, 94, 84, 62, 21, 89, 14, 93, 72, 89, 97, 97, 97, 0, 90, 14];
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = ['"true""false"', 'BST', 'BST-Insert_Delete', 'DoubleLL', 'EmployeList', 'Filemap', 'PC', 'Search_and_replace', 'Vectorfile', 'absolute_value', 'advanced_queue', 'alist', 'array_mmap', 'asm1', 'asm2', 'asm3', 'asm4', 'basic_linked_list', 'bits_leftmost', 'bits_rightmost', 'bits_spin', 'bits_strong', 'bits_sum', 'bitwise-ops', 'bookstore', 'btree-access', 'calloc2', 'cmp_func', 'commandetest', 'count_zero', 'dames', 'factorial', 'fork', 'gcd', 'hexadecimal', 'index-text', 'insertion-sort', 'intersection', 'linked_lists_1', 'linked_lists_2', 'linked_structs', 'main_argc', 'malloc', 'matrix-mult', 'mini-projet-string', 'modem_read', 'modem_read_bk', 'multi-free', 'my-sem', 'my_strlen', 'order_relation_linked_list', 'p3check', 'palindrome', 'pointer_types', 'poly', 'printf', 'reverse', 'rpn-calc', 'run_redir', 's1_ctf1', 's1_ctf2', 's1_diff', 's1_grep', 's1_pipes', 's1_tar', 's2_make', 's2_make_calc', 's2_make_mcq', 's3_cunit_basics', 's3_make', 's3_make_mcq', 's3_make_tests', 's4_file_save_struct', 's4_read_file_array_integer', 's5_big_array_get_set', 's5_file_copy', 's5_file_exists', 'set_bit', 'shell', 'simple_stack', 'sleep_malloc', 'soumission-projet-cracker', 'soumission-projet-fractale', 'stack_vs_heap', 'static_counter', 'strcpy', 'strsplit', 'struct_cmp', 'swap', 'swap2int', 'tab_find', 'tri', 'types', 'types2']
      myChartData.update();
    });


    var ctx = document.getElementById("CountryChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
    gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors


    var myChart = new Chart(ctx, {
      type: 'pie',
      responsive: true,
      legend: {
        display: false
      },
      data: {
        labels: ['LEPL1402', 'LSINF1101', 'LSINF1252'],
        datasets: [{
          label: "Nombre de tâches",
          fill: true,
          backgroundColor: gradientStroke,
          hoverBackgroundColor: gradientStroke,
          borderColor: '#1f8ef1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: [64, 148, 94],
        }]
      },
      options: gradientBarChartConfiguration
    });

  },

  
  showNotification: function(from, align) {
    color = Math.floor((Math.random() * 4) + 1);

    $.notify({
      icon: "tim-icons icon-bell-55",
      message: "Grady"

    }, {
      type: type[color],
      timer: 8000,
      placement: {
        from: from,
        align: align
      }
    });
  }

};
