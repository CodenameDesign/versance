// Replays the captured interaction states in the static replica: menus, dropdowns, calendars, dialogs, tooltips.
// The recorded popup markup is inserted where it appeared in the original, with the recorded enter/exit motion.
(function () {
  'use strict';
  var STATES = [{"id":"s1","parent":null,"kind":"listbox","trigger":{"id":"1061","action":"click","docRect":[1095,5614.88,25,10.5]},"changes":[{"id":"221","name":"style","old":"top: 109px; min-width: 95px; left: 464px; margin-top: 0px;","new":null},{"id":"214","name":"class","old":"itemDepth02233374943__root itemDepth02233374943--isHovered StylableHorizontalMenu3372578893__menuItem itemShared2352141355__menuItem","new":"itemDepth02233374943__root StylableHorizontalMenu3372578893__menuItem itemShared2352141355__menuItem"},{"id":"214","name":"aria-expanded","old":"true","new":"false"},{"id":"212","name":"data-hovered","old":"true","new":null},{"id":"212","name":"data-shown","old":"true","new":null},{"id":"218","name":"class","old":"itemShared2352141355__accessibilityIcon itemShared2352141355--isOpen","new":"itemShared2352141355__accessibilityIcon"},{"id":"1058","name":"class","old":"sqaxP2l sPAw12I sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h","new":"sqaxP2l sPAw12I oeSO0I_--focus sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h"},{"id":"1058","name":"data-focusable-focus","old":"false","new":"true"},{"id":"1058","name":"aria-expanded","old":"false","new":"true"},{"id":"1056","name":"class","old":"sF_7EKY sp78Ud0 sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box swTHtDn","new":"sF_7EKY sp78Ud0 oop7Odd--content-visible sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box swTHtDn"},{"id":"168","name":"class","old":"uZIV9d","new":"uZIV9d Q0rcTZ"},{"id":"1100","name":"class","old":"uZIV9d","new":"uZIV9d Q0rcTZ"}],"roots":[{"id":"s1-0-0","existing":false,"html":"<div data-hook=\"popover-content\" data-content-element=\"popover-content-core-dropdown-undefined\" data-placement=\"bottom\" class=\"sPnSOOu clickOutside958 seiUj0z sVF1lqp\" style=\"position: absolute; z-index: 1000; will-change: transform; top: 0px; left: 0px; transform: translate3d(-1px, 39px, 0px);\" data-pc-i=\"s1-0-0\"><div class=\"\" data-pc-i=\"s1-0-1\"><div class=\"scVjYHl sbmPLQf\" data-hook=\"dropdown-content\" data-pc-i=\"s1-0-2\"><div role=\"listbox\" class=\"s_yoax0\" id=\"dropdown-options-container_-9\" tabindex=\"-1\" data-hook=\"dropdown-content-options-container\" data-pc-i=\"s1-0-3\"><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Public Relations\" data-pc-i=\"s1-0-4\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-5\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-6\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-7\">Public Relations</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Marketing\" data-pc-i=\"s1-0-8\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-9\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-10\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-11\">Marketing</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Legal\" data-pc-i=\"s1-0-12\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-13\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-14\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-15\">Legal</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Investor Relations\" data-pc-i=\"s1-0-16\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-17\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-18\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-19\">Investor Relations</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Finance\" data-pc-i=\"s1-0-20\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-21\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-22\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-23\">Finance</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Communications\" data-pc-i=\"s1-0-24\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-25\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-26\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-27\">Communications</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"CEO\" data-pc-i=\"s1-0-28\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-29\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-30\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-31\">CEO</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Board Member\" data-pc-i=\"s1-0-32\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-33\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-34\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-35\">Board Member</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Other\" data-pc-i=\"s1-0-36\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-37\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-38\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-39\">Other</span></div></div></div></div></div></div></div>","parentId":"1056","beforeId":null,"position":"absolute"}],"timing":{"appearMs":9.4,"settleMs":93.3,"exitMs":7.7},"animations":[],"closeAnimations":[],"startSamples":[{"opacity":"0","transform":"none","visibility":"visible"}],"endSamples":[{"opacity":"1","transform":"matrix(1, 0, 0, 1, -1, 39)","visibility":"visible"}]},{"id":"s2","parent":null,"kind":"popover","trigger":{"id":"1295","action":"click","docRect":[1171.13,849.81,132.06,32]},"changes":[{"id":"1058","name":"class","old":"sqaxP2l sPAw12I oeSO0I_--focus oeSO0I_--focus-visible sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h","new":"sqaxP2l sPAw12I sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--error o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h"},{"id":"1058","name":"data-focusable-focus","old":"true","new":"false"},{"id":"1058","name":"data-focusable-focus-visible","old":"true","new":"false"},{"id":"1058","name":"data-dropdown-base-error","old":"false","new":"true"},{"id":"1058","name":"aria-describedby","old":null,"new":"form-field-error-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-comp-mpx2oh16-"},{"id":"1058","name":"aria-invalid","old":"false","new":"true"},{"id":"1054","name":"class","old":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box oMMt3sv--newErrorMessage s_mowPn scwMXAj s__6VqN23","new":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box oMMt3sv--newErrorMessage oMMt3sv--error s_mowPn scwMXAj s__6VqN23 undefined"},{"id":"1064","name":"class","old":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly s__0oqQvY","new":"slP6sMf oeM_EMx--visible oeM_EMx---errorAppearance-8-TextOnly s__0oqQvY"}],"roots":[{"id":"1064","existing":true,"html":null,"parentId":"1052","beforeId":null,"position":"static"}],"timing":{"appearMs":6.6,"settleMs":164.5,"exitMs":null},"animations":[],"closeAnimations":[],"startSamples":[{"opacity":"1","transform":"none","visibility":"visible"}],"endSamples":[{"opacity":"1","transform":"none","visibility":"visible"}]}];
  var byTrigger = {};
  STATES.forEach(function (s) {
    (byTrigger[s.trigger.id] = byTrigger[s.trigger.id] || []).push(s);
  });
  var open = {};
  var order = [];

  function q(id) {
    return document.querySelector('[data-pc-i="' + id + '"]');
  }
  function docRect(el) {
    var r = el.getBoundingClientRect();
    return [r.left + window.scrollX, r.top + window.scrollY, r.width, r.height];
  }
  function motion(s) {
    var dur = 0;
    var easing = 'ease';
    (s.animations || []).forEach(function (a) {
      if (a.duration + a.delay > dur) {
        dur = a.duration + a.delay;
        easing = a.easing || easing;
      }
    });
    return { dur: dur || s.timing.settleMs || 0, easing: easing };
  }
  function findTrigger(target) {
    for (var e = target; e && e.nodeType === 1; e = e.parentElement) {
      var id = e.getAttribute('data-pc-i');
      if (id && byTrigger[id]) return { el: e, id: id };
    }
    return null;
  }
  function insidePopup(target) {
    for (var i = order.length - 1; i >= 0; i--) {
      var o = open[order[i]];
      for (var k = 0; k < o.els.length; k++) if (o.els[k] && o.els[k].contains(target)) return o;
      for (var j = 0; j < o.state.roots.length; j++) {
        var rr = o.state.roots[j];
        if (rr.existing && q(rr.id) && q(rr.id).contains(target)) return o;
      }
    }
    return null;
  }

  function setAttr(id, name, value) {
    var e = q(id);
    if (!e) return;
    if (value === null || value === undefined) e.removeAttribute(name);
    else e.setAttribute(name, value);
  }

  function openState(s, triggerEl) {
    if (open[s.id]) return;
    var els = [];
    // elements that already existed (a hidden dialog, a trigger's aria-expanded) are changed in place, so their own CSS transitions run
    (s.changes || []).forEach(function (c) {
      setAttr(c.id, c.name, c.new);
    });
    s.roots.forEach(function (r, idx) {
      if (r.existing) {
        var ex = q(r.id);
        if (ex) els.push(null);
        return;
      }
      var t = document.createElement('template');
      t.innerHTML = r.html;
      var el = t.content.firstElementChild;
      var parent = (r.parentId && q(r.parentId)) || document.body;
      var before = r.beforeId ? q(r.beforeId) : null;
      if (before && before.parentNode !== parent) before = null;
      parent.insertBefore(el, before);
      els.push(el);
      if (r.position === 'absolute' && s.trigger.docRect && !el.style.translate) {
        var now = docRect(triggerEl);
        var dx = now[0] - s.trigger.docRect[0];
        var dy = now[1] - s.trigger.docRect[1];
        if (Math.abs(dx) > 0.5 || Math.abs(dy) > 0.5) el.style.translate = dx + 'px ' + dy + 'px';
      }
      var from = s.startSamples && s.startSamples[idx];
      var to = s.endSamples && s.endSamples[idx];
      var m = motion(s);
      if (from && to && m.dur > 0 && (from.opacity !== to.opacity || from.transform !== to.transform) && el.animate) {
        el.animate([{ opacity: from.opacity, transform: from.transform }, { opacity: to.opacity, transform: to.transform }], { duration: m.dur, easing: m.easing });
      }
    });
    open[s.id] = { state: s, els: els, trigger: triggerEl };
    if (s.kind !== 'toggle') order.push(s.id); // Escape and outside clicks close popups, not switched-on controls
  }

  function closeState(id) {
    var o = open[id];
    if (!o) return;
    order.slice().forEach(function (other) {
      if (open[other] && open[other].state.parent === id) closeState(other);
    });
    delete open[id];
    if (order.indexOf(id) >= 0) order.splice(order.indexOf(id), 1);
    var s = o.state;
    (s.changes || []).slice().reverse().forEach(function (c) {
      setAttr(c.id, c.name, c.old);
    });
    var exit = 0;
    (s.closeAnimations || []).forEach(function (a) {
      exit = Math.max(exit, a.duration + a.delay);
    });
    exit = exit || s.timing.exitMs || 0;
    o.els.forEach(function (el, idx) {
      if (!el) return;
      var from = s.endSamples && s.endSamples[idx];
      var to = s.startSamples && s.startSamples[idx];
      var done = function () {
        if (el.parentNode) el.parentNode.removeChild(el);
      };
      if (exit > 0 && from && to && el.animate) {
        var a = el.animate([{ opacity: from.opacity, transform: from.transform }, { opacity: to.opacity, transform: to.transform }], { duration: exit, easing: 'ease-in' });
        a.onfinish = done;
        a.oncancel = done;
      } else done();
    });
  }

  function closeTop() {
    if (!order.length) return false;
    closeState(order[order.length - 1]);
    return true;
  }

  document.addEventListener(
    'click',
    function (e) {
      var trig = findTrigger(e.target);
      if (trig) {
        var states = byTrigger[trig.id].filter(function (s) {
          return s.trigger.action === 'click' && (!s.parent || open[s.parent]);
        });
        if (states.length) {
          var s = states[0];
          if (open[s.id]) closeState(s.id);
          else openState(s, trig.el);
          var a = e.target.closest ? e.target.closest('a') : null;
          if (a && s.kind !== 'toggle') e.preventDefault();
          return;
        }
      }
      var popup = insidePopup(e.target);
      if (popup) {
        if (e.target.closest && e.target.closest('[role=menuitem],[role=option],[role=menuitemradio],[role=menuitemcheckbox]')) {
          var id = popup.state.id;
          setTimeout(function () {
            closeState(id);
          }, 0);
        }
        return;
      }
      if (order.length) {
        var topId = order[order.length - 1];
        if (!(open[topId] && open[topId].trigger.contains(e.target))) closeState(topId);
      }
    },
    true
  );
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && closeTop()) e.stopPropagation();
  }, true);
  document.addEventListener('mouseover', function (e) {
    var trig = findTrigger(e.target);
    if (!trig) return;
    var s = byTrigger[trig.id].filter(function (x) {
      return x.trigger.action === 'hover' && !open[x.id] && (!x.parent || open[x.parent]);
    })[0];
    if (s) openState(s, trig.el);
  });
  document.addEventListener('mouseout', function (e) {
    var trig = findTrigger(e.target);
    if (!trig) return;
    if (e.relatedTarget && trig.el.contains(e.relatedTarget)) return;
    byTrigger[trig.id].forEach(function (s) {
      if (s.trigger.action === 'hover' && open[s.id] && !(e.relatedTarget && open[s.id].els.some(function (x) { return x && x.contains(e.relatedTarget); }))) closeState(s.id);
    });
  });

  window.__PC_REPLICA = { states: STATES, openIds: function () { return order.slice(); } };
})();
