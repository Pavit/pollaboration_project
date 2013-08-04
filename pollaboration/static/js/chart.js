// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

  window.pollChart.helpers = {
    get: function(key, fn) {
      return function(d) {
        var val;
        val = key ? d[key] : d;
        if (fn) {
          return fn(val);
        } else {
          return val;
        }
      };
    }
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

  window.pollChart.legend = function(_arg) {
    var colorKey, colorScale, data, el, g, holder, labelKey;
    colorScale = _arg.colorScale, el = _arg.el, data = _arg.data, labelKey = _arg.labelKey, colorKey = _arg.colorKey;
    if (colorKey == null) {
      colorKey = labelKey;
    }
    holder = el.append("div").attr("class", "legendHolder");
    g = holder.selectAll(".legend").data(data).enter().append("div").attr("class", "legend");
    g.append("span").style("background", function(d) {
      return colorScale(d[colorKey]);
    }).attr("class", "key");
    return g.append("span").text(function(d) {
      return d[labelKey];
    }).attr("class", "label");
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

  window.pollChart.legend2 = function(_arg) {
    var colorKey, colorScale, data, el, g, getChecked, handler, holder, labelKey, valueKey;
    colorScale = _arg.colorScale, el = _arg.el, data = _arg.data, labelKey = _arg.labelKey, colorKey = _arg.colorKey, valueKey = _arg.valueKey, handler = _arg.handler;
    console.log(arguments);
    if (colorKey == null) {
      colorKey = labelKey;
    }
    if (handler == null) {
      handler = function() {};
    }
    getChecked = function() {
      data = _.compact(g.selectAll("input:checked").map(function(a) {
        var _ref, _ref1;
        return (_ref = a[0]) != null ? (_ref1 = _ref.__data__) != null ? _ref1[labelKey] : void 0 : void 0;
      }));
      if (data.length === 0) {
        this.checked = true;
        data = [this.__data__[labelKey]];
      }
      if (this.checked) {
        d3.select(this.parentNode).attr("class", "legend2").transition().duration(500).style("background-color", function(d) {
          return colorScale(d[colorKey]);
        });
      } else {
        d3.select(this.parentNode).attr("class", "legend2 disabled").transition().duration(500).style("background-color", "rgb(200,200,200)");
      }
      return handler(data);
    };
    holder = el.append("div").attr("class", "legendHolder");
    g = holder.selectAll(".legend2").data(data).enter().append("label").attr("class", "legend2").style("background-color", function(d) {
      return colorScale(d[colorKey]);
    });
    g.append("input").attr("type", "checkbox").attr("checked", "checked").on("change", getChecked);
    g.append("span").text(function(d) {
      return d[valueKey];
    }).attr("class", "value");
    return g.append("span").text(function(d) {
      return d[labelKey];
    }).attr("class", "label");
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

// Controls Pie Legend/Toggle
  window.pollChart.legend3 = function(_arg) {
    var colorKey, colorScale, data, el, g, getChecked, handler, holder, labelKey, switcher, valueKey;
    colorScale = _arg.colorScale, el = _arg.el, data = _arg.data, labelKey = _arg.labelKey, colorKey = _arg.colorKey, valueKey = _arg.valueKey, handler = _arg.handler;
    if (colorKey == null) {
      colorKey = labelKey;
    }
    if (handler == null) {
      handler = function() {};
    }
    getChecked = function() {
      var $this;
      $this = d3.select(this).select(".switcher");
      if ($this.attr("class").indexOf("active") === -1) {
        $this.attr("class", "switcher active");
        d3.select(this).attr("class", "legend2").transition().duration(500).style("background-color", function(d) {
          return colorScale(d[colorKey]);
        });
      } else {
        $this.attr("class", "switcher");
        d3.select(this).attr("class", "legend2 disabled").transition().duration(500).style("background-color", "rgb(87,87,87)");
      }
      data = _.compact(g.selectAll(".active").map(function(a) {
        var _ref, _ref1;
        return (_ref = a[0]) != null ? (_ref1 = _ref.__data__) != null ? _ref1[labelKey] : void 0 : void 0;
      }));
      return handler(data);
    };
    holder = el.append("div").attr("class", "legendHolder");
    g = holder.selectAll(".legend2").data(data).enter().append("label").attr("class", "legend2").style("background-color", function(d) {
      return colorScale(d[colorKey]);
    }).on("click", getChecked);
    switcher = g.append("div").attr("class", "switcher active");
    // switcher.append("span").attr("class", "onText").text("ON"); //Controls ON/OFF switches for toggles.
    // switcher.append("span").attr("class", "offText").text("OFF");
    // switcher.append("span").attr("class", "blackRect");
    g.append("span").text(function(d) {
      return d[valueKey];
    }).attr("class", "value");
    return g.append("span").text(function(d) {
      return d[labelKey];
    }).attr("class", "answer pull-right"); //Controls text for toggles.
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

  window.pollChart.tooltip = function(parent, selection, getter) {
    var tooltip, tooltipMove, tooltipOut, tooltipOver;
    tooltip = d3.select('body').append("div").attr("class", "tooltip").style("opacity", 0);
    tooltipOver = function(d) {
      d3.select(this).style({
        "opacity": 0.8
      });
      tooltip.transition().duration(200).style("opacity", 0.9);
      return tooltip.html(getter(d));
    };
    tooltipMove = function() {
      return tooltip.style("left", (d3.event.pageX + 10) + "px").style("top", (d3.event.pageY - 10) + "px");
    };
    tooltipOut = function() {
      d3.select(this).style({
        "opacity": 1
      });
      return tooltip.transition().duration(200).style("opacity", 0);
    };
    return selection.on("mouseover", tooltipOver).on("mouseout", tooltipOut).on("mousemove", tooltipMove);
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
(function() {
  if (window.pollChart == null) {
    window.pollChart = {};
  }

  window.pollChart.tooltipBubble = function(parent, selection, getter) {
    var span, svg, tooltip, tooltipMove, tooltipOut, tooltipOver;
    tooltip = d3.select("body").append("div").attr("class", "tooltip").style("opacity", 0);
    span = tooltip.append("span");
    svg = tooltip.append("svg");
    svg.append("path").attr("class", "tooltip").attr("d", d3.svg.symbol("triangle-down"));
    tooltipOver = function(d) {
      d3.select(this).style({
        "opacity": 0.7
      });
      tooltip.transition().duration(200).style("opacity", 0.9);
      return span.html(getter(d));
    };
    tooltipMove = function() {
      return tooltip.style("left", (d3.event.layerX + 20) + "px").style("top", (d3.event.layerY - 10) + "px");
    };
    tooltipOut = function() {
      d3.select(this).style({
        "opacity": 1
      });
      return tooltip.transition().duration(200).style("opacity", 0);
    };
    return selection.on("mouseover", tooltipOver).on("mouseout", tooltipOut).on("mousemove", tooltipMove);
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
/*

  Grid Chart

  Data should be of the form:
  [
    {question: "Some Question"
     answers: [
      {id: 1, label: "Some Answer", value:2000}
      {id: 2, label: "Some Answer2", value:400}
      {id: 3, label: "Some Answer3", value:500}
     chosen: 2
  ]
*/


(function() {
  var defaults;

  if (window.pollChart == null) {
    window.pollChart = {};
  }

  defaults = {
    height: 60,
    margin: {
      top: 0,
      right: 0,
      bottom: 30,
      left: 0
    },
    colors: ["#FFF5E4", "#FF7E65", "#7DCDFC", "#4a9acd", "#3D444B"],
    data: []
  };

  window.pollChart.grid = function(opts) {
    var answer, answers, chart, colors, data, el, get, getter, height, helpers, index, item, margin, pollChart, tooltip, width, _i, _j, _len, _len1, _ref;
    pollChart = window.pollChart;
    helpers = pollChart.helpers;
    get = helpers.get;
    tooltip = pollChart.tooltip;
    opts = _.defaults(opts, defaults);
    if (opts.width == null) {
      opts.width = d3.select(opts.el).node().offsetWidth;
    }
    margin = opts.margin, width = opts.width, height = opts.height;
    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;
    colors = opts.colors;
    data = [];
    _ref = opts.data;
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      item = _ref[_i];
      answers = _.sortBy(item.answers, "value");
      for (index = _j = 0, _len1 = answers.length; _j < _len1; index = ++_j) {
        answer = answers[index];
        if (answer.id === item.chosen) {
          data.push({
            question: item.question,
            answer: answer.label,
            color: colors[index],
            question_id: item.question_id
          });
          break;
        }
      }
    }
    el = d3.select(opts.el);
    chart = el.selectAll(".gridSquare").data(data).enter().append("div").attr("class", "gridSquare").style("background", get("color"));
/*    getter = function(d) {
      return "Q. " + d.question + " <br />\nA. " + d.answer;
    };
    return tooltip(el, chart, getter);*/
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
/*

  Horizontal Stacked Chart

  Data should be of the form:
  [
    {label: "Some Answer", value:2000}
  ]
*/


(function() {
  var defaults;

  if (window.pollChart == null) {
    window.pollChart = {};
  }

  defaults = {
    height: 60,
    margin: {
      top: 0,
      right: 0,
      bottom: 0,
      left: 0
    },
    colors: ["#FFF5E4", "#FF7E65", "#7DCDFC", "#4a9acd", "#3D444B"],
    data: []
  };

  window.pollChart.stacked = function(opts) {
    var chart, color, data, el, get, group, height, helpers, item, margin, percent, pollChart, scale, start, svg, tooltip, total, width, _i, _len;
    pollChart = window.pollChart;
    helpers = pollChart.helpers;
    get = helpers.get;
    tooltip = pollChart.tooltip;
    opts = _.defaults(opts, defaults);
    if (opts.width == null) {
      opts.width = d3.select(opts.el).node().offsetWidth;
    }
    margin = opts.margin, width = opts.width, height = opts.height, data = opts.data;
    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;
    total = d3.sum(data, get("value"));
    scale = d3.scale.linear().range([0, width]).domain([0, total]);
    color = d3.scale.ordinal().range(opts.colors);
    start = 0;
    for (_i = 0, _len = data.length; _i < _len; _i++) {
      item = data[_i];
      item.start = start;
      percent = Math.round(item.value / total * 100);
      item.tooltip = "" + item.label + " (" + percent + "%)";
      start += item.value;
    }
    el = d3.select(opts.el);
    svg = el.append("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom).append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    group = svg.selectAll("g").data(data, get("label")).enter().append("g");
    chart = group.append("rect").attr("class", "stack").style("fill", get("label", color)).attr("height", height).attr("x", get("start", scale)).attr("width", get("value", scale));
    return tooltip(el, chart, get("tooltip"));
  };

}).call(this);
// Generated by CoffeeScript 1.6.3
/*

  Sunburst Chart

  Data should be of the form:
*/


(function() {
  var defaults, get, getOptions, handle, insertLinebreaks, log, sum, textTransform, transformData,
    __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  if (window.pollChart == null) {
    window.pollChart = {};
  }

  defaults = {
    width: 400,
    height: 400,
    colors: ["#c3c3c3", "#FF7E65", "#7DCDFC", "#4a9acd", "#3D444B"],
    margin: {
      top: 200,
      right: 0,
      bottom: 0,
      left: 0
    },
    data: [],
    labels: [],
    fields: [],
    opacityBase: 1.0,
    opacityInner: 0.5,
    opacityOuter: 0.1
  };

  sum = function(array, key) {
    var item, total, _i, _len;
    total = 0;
    for (_i = 0, _len = array.length; _i < _len; _i++) {
      item = array[_i];
      total += item[key];
    }
    return total;
  };

  get = function(key, fn) {
    return function(d) {
      var a;
      a = d[key];
      if (fn) {
        return fn(a);
      } else {
        return a;
      }
    };
  };

// Sunburst Label Linebreaks
  insertLinebreaks = function(d) {
    var i, textElem, tspan, word, words, _ref, _ref1, _ref2, _results;
    textElem = d3.select(this);
    words = d.name.split(" ");
    textElem.text("");
    i = 0;
    _results = [];
    while (words.length) {
      word = [(_ref = words.shift()) != null ? _ref : "", (_ref1 = words.shift()) != null ? _ref1 : "", (_ref2 = words.shift()) != null ? _ref2 : ""].join(" ");
      tspan = textElem.append("tspan").text(word);
      if (i > 0) {
        tspan.attr("x", 0).attr("dy", "15");
      }
      _results.push(i++);
    }
    return _results;
  };

// Sunburst Label Positioning

  angle = function(d) {
          var a = (d.startAngle + d.endAngle) * 90 / Math.PI - 90;
          return a > 90 ? a - 180 : a;
  };

  textTransform = function(arc, radius) {
    return function(d) {
      var c, h, x, y;
      c = arc.centroid(d);
      x = c[0];
      y = c[1];
      h = Math.sqrt(x * x + y * y); // Oh shit its the pythagorean theorem!
      return "translate(" + (x / h * labelr) + "," + (y / h * labelr) + ")rotate(" + 0 + ")";
    };
  };

  handle = function(items, key, last, answer, total, parent) {
    var children, name, o, out, _ref;
    out = [];
    _ref = _.groupBy(items, key);
    for (name in _ref) {
      children = _ref[name];
      o = {
        name: name,
        answer: answer
      };
      o.id = name + answer + key + parent.name;
      o.size = sum(children, "count");
      o.percent = "" + (Math.round(o.size / total * 100)) + "%";
      if (!last) {
        o.children = children;
      }
      out.push(o);
    }
    return out;
  };

  transformData = function(data, fields, answers, from, to) {
    var child, cloned, filtered, grandchild, item, o;
    if (fields == null) {
      fields = [];
    }
    if (answers == null) {
      answers = [];
    }
    if (from == null) {
      from = 0;
    }
    if (to == null) {
      to = Infinity;
    }
    filtered = {
      value: 0
    };
    filtered.answers = (function() {
      var _i, _len, _ref, _ref1, _results;
      _ref = data.answers;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        item = _ref[_i];
        if (!((_ref1 = item.answer, __indexOf.call(answers, _ref1) >= 0))) {
          continue;
        }
        cloned = _.clone(item);
        cloned.data = _.filter(item.data, function(a) {
          var _ref2;
          return (from < (_ref2 = a.date) && _ref2 < to);
        });
        cloned.count = sum(cloned.data, "count");
        filtered.value += cloned.count;
        _results.push(cloned);
      }
      return _results;
    })();
    return {
      name: data.question,
      size: filtered.value,
      children: (function() {
        var _i, _j, _k, _len, _len1, _len2, _ref, _ref1, _ref2, _results;
        _ref = filtered.answers;
        _results = [];
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          item = _ref[_i];
          o = {
            name: item.answer,
            answer: item.answer,
            size: item.count,
            id: item.answer,
            percent: "" + (Math.round(item.count / filtered.value * 100)) + "%"
          };
          if (fields.length) {
            o.children = handle(item.data, fields[0], fields.length === 1, item.answer, item.count, item);
            if (fields.length > 1) {
              _ref1 = o.children;
              for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
                child = _ref1[_j];
                child.children = handle(child.children, fields[1], fields.length === 2, item.answer, child.size, child);
                if (fields.length > 2) {
                  _ref2 = child.children;
                  for (_k = 0, _len2 = _ref2.length; _k < _len2; _k++) {
                    grandchild = _ref2[_k];
                    grandchild.children = handle(grandchild.children, fields[2], true, item.answer, grandchild.size, grandchild);
                  }
                }
              }
            }
          }
          _results.push(o);
        }
        return _results;
      })()
    };
  };

  log = function() {
    return console.log.apply(console, arguments);
  };

  getOptions = function(answers, field) {
    return _.chain(answers).pluck("data").flatten().pluck(field).unique().value();
  };

  window.pollChart.sunburst = function(opts) {
    var answerP, answers, arc, arc2, arcTween, change, clearHighlights, clickHandler1, clickHandler2, clicked, clicked2, color, data, divs, draw, el, field, filters, getSize, height, helpers, index, innerRadius, label, legend, margin, old, options, outerRadius, partition, pollChart, radius, selected, selects, sliderDiv, sliderSpan, stash, stashEnter, svg, tooltip, tooltip1, tooltip2, tooltip3, tooltipMove, tooltipOut, tooltipOver, update, width, writeLabel, writeLabel2, _i, _len, _ref, _ref1;
    pollChart = window.pollChart;
    helpers = pollChart.helpers;
    get = helpers.get;
    legend = pollChart.legend3;
    opts = _.defaults(opts, defaults);
    margin = opts.margin, width = opts.width, height = opts.height;
    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;
    radius = Math.min(width, height) / 2;
    labelr = radius * 0.25 // Label
   /* color = d3.scale.ordinal().range(colorbrewer.RdYlBu[5]);*/
    color = d3.scale.ordinal().range(opts.colors);
    answers = _.pluck(opts.data.answers, "answer");
    data = transformData(opts.data, [], answers);
    options = [];
    _ref = opts.fields;
    for (index = _i = 0, _len = _ref.length; _i < _len; index = ++_i) {
      field = _ref[index];
      label = (_ref1 = opts.labels[index]) != null ? _ref1 : field;
      options.push({
        label: label,
        field: field
      });
    }
    options = ["Blank"].concat(_.compact(options));
    partition = d3.layout.partition().sort(null).size([2 * Math.PI, radius * radius * 0.5]).value(get("size"));
    innerRadius = function(d) {
      if (d.depth === 1) {
        return 0;
      } else {
        return Math.sqrt(d.y);
      }
    };
    outerRadius = function(d) {
      return Math.sqrt(d.y + d.dy);
    };
    arc = d3.svg.arc().startAngle(function(d) {
      return d.x;
    }).endAngle(function(d) {
      return d.x + d.dx;
    }).innerRadius(innerRadius).outerRadius(outerRadius);
    arc2 = d3.svg.arc().startAngle(function(d) {
      return d.x + (d.dx / 2);
    }).endAngle(function(d) {
      return d.x + (d.dx / 2) + 0.01;
    }).innerRadius(innerRadius).outerRadius(outerRadius);
    el = d3.select(opts.el);
    el.append("h2").text(opts.data.question);
    answerP = el.append("p").text(opts.data.value + " Answers");
    svg = el.append("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom).append("g").attr("transform", "translate(" + width * 0.5 + "," + height * 0.5 + ")");
    
    //label = el.append("span").attr("class", "poll-label");
    old = null;

    //  Inner Ring Click
    //clicked = [];
    //clicked2 = [];
    // clickHandler2 = function(d2) {
    //   var $grandparent, $parent, $this, group, parents, turnOff, wrongParent;
    //   $this = d3.select(this);
    //   group = svg.selectAll("g");
    //   $parent = group.filter(function(d) {
    //     return d === d2.parent;
    //   });
    //   $grandparent = group.filter(function(d) {
    //     return d === d2.parent.parent;
    //   });
    //   if (__indexOf.call(clicked2, d2) >= 0) {
    //     clicked2 = _.without(clicked2, d2);
    //     return $this.attr("opacity", 1);
    //   } else {
    //     clicked2.push(d2);
    //     $this.attr("opacity", opts.opacityOuter);
    //     wrongParent = _.filter(clicked2, function(d) {
    //       return d.parent.parent !== d2.parent.parent;
    //     });
    //     if (wrongParent.length) {
    //       clicked2 = _.difference(clicked2, wrongParent);
    //       group.filter(function(d) {
    //         return __indexOf.call(wrongParent, d) >= 0;
    //       }).attr("opacity", 1);
    //     }
    //     parents = _.pluck(clicked2, "parent");
    //     turnOff = _.difference(clicked, parents);
    //     if (turnOff.length) {
    //       turnOff = turnOff.concat(_.pluck(turnOff, "parent"));
    //       group.filter(function(d) {
    //         return __indexOf.call(turnOff, d) >= 0;
    //       }).attr("opacity", 1);
    //     }
    //     clicked = [d2.parent];
    //     $parent.attr("opacity", opts.opacityInner);
    //     return $grandparent.attr("opacity", opts.opacityBase);
    //   }
    // };
    // getSize = function(d) {
    //   return d.size;
    // };

    // Additive Label
    // writeLabel = function() {
    //   var grouped, key, keySum, out, total, vals;
    //   out = "";
    //   total = d3.sum(_.unique(_.pluck(clicked, "parent")), getSize);
    //   grouped = _.groupBy(clicked, "name");
    //   for (key in grouped) {
    //     vals = grouped[key];
    //     keySum = d3.sum(vals, getSize);
    //     out += "" + key + " - (" + (Math.round(keySum / total * 100)) + "%) ";
    //   }
    //   return label.text(out);
    // };
    // writeLabel2 = function() {
    //   var grouped, key, keySum, out, total, vals;
    //   out = "";
    //   total = d3.sum(_.unique(_.pluck(clicked2, "parent")), getSize);
    //   grouped = _.groupBy(clicked2, "name");
    //   for (key in grouped) {
    //     vals = grouped[key];
    //     keySum = d3.sum(vals, getSize);
    //     out += "" + key + " - (" + (Math.round(keySum / total * 100)) + "%) ";
    //   }
    //   return label.text(out);
    // };

// Tooltips
/*    tooltip1 = function(d) {
      return "<strong>" + d.answer + "</strong>, " + d.percent + " (" + d.size + ")";
    };
    tooltip2 = function(d) {
      return "<strong>" + d.name + "</strong>, " + d.percent + " (" + d.size + ") of<br />" + (tooltip1(d.parent));
    };
    tooltip3 = function(d) {
      return "<strong>" + d.name + "</strong>, " + d.percent + " (" + d.size + ") of<br />" + (tooltip2(d.parent));
    };
    tooltip = d3.select('body').append("div").attr("class", "tooltip suntip").style("opacity", 0);
    tooltipOver = function(d) {
      tooltip.transition().duration(200).style("opacity", 0.9);
      return tooltip.html((function() {
        switch (d.depth) {
          case 1:
            return tooltip1(d);
          case 2:
            return tooltip2(d);
          case 3:
            return tooltip3(d);
          default:
            return "";
        }
      })());
    };
    tooltipMove = function() {
      return tooltip.style("left", (d3.event.pageX + 10) + "px").style("top", (d3.event.pageY - 10) + "px");
    };
    tooltipOut = function() {
      return tooltip.style("opacity", 0);
    };*/

    // Outer Ring Click
    // clickHandler1 = function(d1) {
    //   var $parent, $this, _ref2;
    //   $this = d3.select(this);
    //   $parent = svg.selectAll("g").filter(function(d) {
    //     return d === d1.parent;
    //   });
    //   if (__indexOf.call(clicked, d1) >= 0) {
    //     clicked = _.without(clicked, d1, d1.parent);
    //     $this.attr("opacity", 1);
    //     if (_ref2 = d1.parent, __indexOf.call(_.pluck(clicked, "parent"), _ref2) < 0) {
    //       $parent.attr("opacity", 1);
    //     }
    //   } else {
    //     clicked.push(d1);
    //     $this.attr("opacity", opts.opacityInner);
    //     $parent.attr("opacity", opts.opacityBase);
    //   }
    //   if (clicked2.length) {
    //     svg.selectAll("g").filter(function(d) {
    //       return __indexOf.call(clicked2, d) >= 0;
    //     }).attr("opacity", 1);
    //     return clicked2 = [];
    //   }
    // };

    // Clearing Highlights
    // clearHighlights = function() {
    //   clicked = [];
    //   clicked2 = [];
    //   label.text("");
    //   return svg.selectAll("g").attr("opacity", 1);
    // };
    old = {};
    stash = function(d) {
      return old[d.id] = {
        x: d.x,
        dx: d.dx,
        y: d.y,
        dy: d.dy
      };
    };
    stashEnter = function(d) {
      var middle;
      middle = d.x + (d.dx / 2);
      return old[d.id] = {
        x: middle,
        dx: 0.01
      };
    };
    arcTween = function(a) {
      var i;
      i = d3.interpolate(old[a.id], a);
      return function(t) {
        var b;
        b = i(t);
        return arc(b);
      };
    };

    // Controls Drawing of Chart
    draw = function(data) {
      var enter, exit, exitTrans, group;
      data = partition.nodes(data);
      group = svg.selectAll("g").data(data, get("id"));
      enter = group.enter().append("g");
      exit = group.exit();
      exitTrans = exit.transition().duration(1000).remove();
      exitTrans.select("path").style("opacity", 0);
      exitTrans.select("text").style("opacity", 0);
      enter.filter(function(d) {
        return d.depth;
      }).append("path").style("stroke", "#fff").style("fill", get("answer", color)).style("opacity", 0).attr("d", arc2).each(stashEnter);
      group.select("path").transition().duration(1000).attrTween("d", arcTween).style("opacity", 1).each("end", stash);
      enter.filter(function(d) { //Beginning of Pie Chart Labels
        return d.depth === 1;
      }).append("text").text(function(d) {
        return d.name;
      }).attr("dy", ".35em").style("text-anchor", "middle").each(insertLinebreaks).style("opacity", 1);
      group.select("text").transition().duration(1000).attr("transform", textTransform(arc, radius)); //End of Pie Chart Labels
      group.filter(function(d) {
        return d.depth === 3;
      }).style("opacity", opts.opacityOuter).on("click", clickHandler2);
      group.filter(function(d) {
        return d.depth === 2;
      }).style("opacity", opts.opacityInner).on("click", clickHandler1);
      group.filter(function(d) {
        return d.depth === 1;
      }).style("opacity", opts.opacityBase).on("click", clearHighlights);
      return group.on("mouseover", tooltipOver).on("mouseout", tooltipOut).on("mousemove", tooltipMove);
    };
    draw(data);
    sliderSpan = el.append("p").attr("class", "slider-text").text("Range: ").append("span");
    sliderSpan.text(moment.unix(opts.data.start).format("ll") + " to " + moment.unix(opts.data.end).format("ll"));
    sliderDiv = el.append("div").attr("class", "slider").node();
    legend({
      el: el,
      colorScale: color,
      data: data.children,
      labelKey: "name",
      colorKey: "answer",
      valueKey: "percent",
      handler: function(data) {
        answers = data;
        return update();
      }
    });
    filters = [
      {
        options: options
      }, {
        options: options
      }
    ];
    el.append("h4").text("Filters: ");
    divs = el.selectAll(".filter").data(filters).enter().append("div").attr("class", "filter");
    selected = [];
    change = function(d, i) {
      selected[i] = this.options[this.selectedIndex].__data__.field;
      return update();
    };
    selects = divs.append("select").on("change", change);
    selects.selectAll("option").data(get("options")).enter().append("option").text(get("label"));
    update = function() {
      data = transformData(opts.data, _.compact(selected), answers);
      return draw(data);
    };
    return jQuery(sliderDiv).slider({
      range: true,
      min: opts.data.start,
      max: opts.data.end,
      values: [opts.data.start, opts.data.end],
      slide: function(event, ui) {
        return sliderSpan.text(moment.unix(ui.values[0]).format("LL") + " to " + moment.unix(ui.values[1]).format("LL"));
      },
      stop: function(event, ui) {
        data = transformData(opts.data, _.compact(selected), answers, ui.values[0], ui.values[1]);
        answerP.text(data.size + " Answers");
        return draw(data);
      }
    });
  };

  window.pollChart.showSunburst = function(source, selector) {
    var height, opts, width;
    if (selector == null) {
      selector = "#sunburst";
    }
    width = height = d3.select(selector).html("").node().offsetWidth;
    opts = {
      el: selector,
      fields: ["gender", "agegroup", "political"],
      labels: ["Gender", "Age Group", "Politics"],
      colors: ["#c3c3c3", "#FF7E65", "#7DCDFC", "#4a9acd", "#68798a"],
      opacityBase: 1.0,
      opacityInner: 0.75,
      opacityOuter: 0.5,
      width: width,
      height: height,
      margin: {
        top: -100,
        right: 0,
        bottom: 0,
        left: 0
      }
    };
    if (_.isString(source)) {
      return d3.json(source, function(err, data) {
        if (!err) {
          opts.data = data;
          return pollChart.sunburst(opts);
        }
      });
    } else {
      opts.data = source;
      return pollChart.sunburst(opts);
    }
  };

}).call(this);