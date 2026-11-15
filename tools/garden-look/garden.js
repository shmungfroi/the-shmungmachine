<script>
/* EXP 0.3.20 Garden Look: background layer, focus-mode crown, module tracking */
(()=>{
  const bg=document.createElement('div');bg.id='gardenBg';bg.setAttribute('aria-hidden','true');
  bg.innerHTML='<i class="g-wash"></i><i class="g-lattice"></i><i class="g-crown"></i><i class="g-rule"></i>';
  document.body.prepend(bg);
  const dp=document.querySelector('.daybreak-instrument-panel');
  if(dp){const c=document.createElement('div');c.id='gardenFocusCrown';c.setAttribute('aria-hidden','true');dp.parentNode.insertBefore(c,dp);}
  const sync=()=>{const t=document.querySelector('nav.tabs .tab.active');const focus=document.body.classList.contains('daybreak-focus-mode');
    document.documentElement.dataset.gmod=focus?'daybreak':(t&&t.dataset.tab)||'daybreak';};
  sync();
  const mo=new MutationObserver(sync);
  document.querySelectorAll('nav.tabs .tab').forEach(t=>mo.observe(t,{attributes:true,attributeFilter:['class']}));
  mo.observe(document.body,{attributes:true,attributeFilter:['class']});
})();
</script>
