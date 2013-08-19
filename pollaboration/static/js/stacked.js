
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
    holder = d3.select("#legendplacement").append("div").attr("class", "legendHolder");
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

      return draw(data);
    };
    holder = d3.select("#legendplacement").append("div").attr("class", "legendHolder");
    g = holder.selectAll(".legend2").data(data).enter().append("label").attr("class", "legend2").style("background-color", function(d) {
      return colorScale(d[colorKey]);
    });
    g.append("input").attr("type", "checkbox").attr("checked", "checked").on("change", getChecked);
/*    g.append("span").text(function(d) {
      return d[valueKey];
    }).attr("class", "value");*/
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
          return colorScale(d[colorKey]); });
        $(this).find(".toggleText").empty().text("ON");
      } else {
        $this.attr("class", "switcher");
        d3.select(this).attr("class", "legend2 disabled").transition().duration(500).style("background-color", "rgb(87,87,87)");
        $(this).find(".toggleText").empty().text("OFF");
      }
      data = _.compact(g.selectAll(".active").map(function(a) {
        var _ref, _ref1;
        return (_ref = a[0]) != null ? (_ref1 = _ref.__data__) != null ? _ref1[labelKey] : void 0 : void 0;
      }));
      console.log("get checked data");
      console.log(data);
      return handler(data);
    }; //end of getChecked

    holder = d3.select("#legendplacement").append("div").attr("class", "legendHolder");
    g = holder.selectAll(".legend2").data(data).enter().append("label").attr("class", "legend2").style("background-color", function(d) {
      return colorScale(d[colorKey]);
    }).on("click", getChecked);
    switcher = g.append("div").attr("class", "switcher active");
    switcher.append("span").attr("class", "toggleText").text("ON"); //Controls ON/OFF switches for toggles.
    //switcher.append("span").attr("class", "text").text("OFF");
    //switcher.append("span").attr("class", "blackRect");
/*    g.append("span").text(function(d) {
      return d[valueKey];
    }).attr("class", "value");*/
    return g.append("span").text(function(d) {
      return d[labelKey];
    }).attr("class", "answer"); //Controls text for toggles.
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
      tooltip.transition().duration(200).style("opacity", 0);
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
    // tooltip = pollChart.tooltip;
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
      // item.tooltip = "" + item.label + " (" + percent + "%)";
      start += item.value;
    }
    el = d3.select(opts.el);
    svg = el.append("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom).append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    group = svg.selectAll("g").data(data, get("label")).enter().append("g");
    chart = group.append("rect").attr("class", "stack").style("fill", get("label", color)).attr("height", height).attr("x", get("start", scale)).attr("width", get("value", scale));
    // return tooltip(el, chart, get("tooltip"));
  };

}).call(this);