
(function(){
  var toast=document.getElementById('toast');
  function showToast(msg){
    toast.textContent=msg;
    toast.setAttribute('aria-hidden','false');
    toast.classList.add('show');
    clearTimeout(showToast._t);
    showToast._t=setTimeout(function(){toast.classList.remove('show');toast.setAttribute('aria-hidden','true');},2400);
  }
  var CDN='https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/';

  // Stations data
  var stations=[
    {name:'特来电杭州中心站',badge:'PLUS',badgeCls:'plus',addr:'西湖区文三路 478 号',d:'0.8km',rate:'4.9',
      fast:{n:6,total:8},slow:{n:2,total:4},price:'1.28',discount:'PLUS 价 0.98'},
    {name:'星星充电 · 黄龙站',badge:'NFC',badgeCls:'nfc',addr:'西湖区黄龙体育中心 B 区',d:'1.2km',rate:'4.7',
      fast:{n:3,total:6},slow:{n:0,total:2},price:'1.35',discount:'即插即充'},
    {name:'云快充 · 西湖银泰站',badge:'即插即充',badgeCls:'nfc',addr:'上城区延安路 98 号',d:'1.6km',rate:'4.8',
      fast:{n:0,total:4},slow:{n:5,total:8},price:'1.20',discount:'停车首小时免费'},
    {name:'国网 · 高速服务区站',badge:'高速',badgeCls:'plus',addr:'G2504 高速绕城服务区',d:'3.4km',rate:'4.5',
      fast:{n:2,total:4},slow:{n:0,total:0},price:'1.45',discount:'24小时营业'}
  ];
  function renderStations(){
    var html='';
    stations.forEach(function(s){
      html+='<article class="station">'+
        '<div class="st-top"><div style="min-width:0">'+
          '<div class="st-name">'+s.name+'<span class="badge '+s.badgeCls+'">'+s.badge+'</span></div>'+
          '<div class="st-addr"><img class="icon" src="'+CDN+'map-pin.svg" alt="" width="14" height="14"><span>'+s.addr+'</span></div>'+
        '</div>'+
        '<div class="rating"><img class="icon" src="'+CDN+'star.svg" alt="" width="14" height="14">'+s.rate+'</div></div>'+
        '<div class="st-mid">'+
          '<div class="meter"><b class="green num">'+s.fast.n+'</b><span>'+s.fast.total+' 快充空闲</span></div>'+
          '<div class="meter"><b class="orange num">'+s.slow.n+'</b><span>'+s.slow.total+' 慢充空闲</span></div>'+
          '<div class="st-price"><span class="unit">¥</span><span class="yuan num">'+s.price+'</span><span class="unit">/度</span></div>'+
        '</div>'+
        '<div class="st-actions">'+
          '<button class="btn-nav navit" data-addr="'+s.addr+'" aria-label="导航到 '+s.name+'"><img class="icon" src="'+CDN+'navigation.svg" alt="" width="15" height="15">导航</button>'+
          '<button class="btn-charge charge" data-station="'+s.name+'" aria-label="在 '+s.name+' 充电"><img class="icon" src="'+CDN+'zap.svg'" alt="" width="15" height="15">充电</button>'+
        '</div></article>';
    });
    document.getElementById('stationList').innerHTML=html;
  }
  renderStations();

  // view switch
  var mapV=document.getElementById('mapView'),listV=document.getElementById('listView');
  function setView(map){
    mapV.classList.toggle('active',map);listV.classList.toggle('active',!map);
    mapV.setAttribute('aria-pressed',map?'true':'false');listV.setAttribute('aria-pressed',(!map)?'true':'false');
  }
  mapV.addEventListener('click',function(){setView(true);showToast('已切换地图视图…');});
  listV.addEventListener('click',function(){setView(false);});

  // filter
  document.getElementById('filterBtn').addEventListener('click',function(){showToast('筛选：快充 / 免费停车 / 高速 / 重卡…');});

  // nav
  document.querySelectorAll('.navit').forEach(function(b){b.addEventListener('click',function(){showToast('正在为你导航至「'+b.dataset.addr+'」…');});});

  // charge -> sheet
  var sheet=document.getElementById('sheet');
  function openSheet(name){sheet.classList.add('open');document.body.style.overflow='hidden';
    document.getElementById('sheetTitle').textContent='确认充电参数 · '+name;}
  function closeSheet(){sheet.classList.remove('open');document.body.style.overflow='';}
  document.querySelectorAll('.charge').forEach(function(b){b.addEventListener('click',function(){openSheet(b.dataset.station);});});
  document.getElementById('scanBtn').addEventListener('click',function(){openSheet('扫码识别 云快充 枪 A-03');});
  document.getElementById('tabScan').addEventListener('click',function(){openSheet('扫码识别 特来电 枪 B-07');});
  document.getElementById('actScan').addEventListener('click',function(){openSheet('扫码识别 星星充电 枪 C-02');});
  sheet.querySelector('[data-close]').addEventListener('click',closeSheet);
  sheet.addEventListener('keydown',function(e){if(e.key==='Escape')closeSheet();});

  // confirm
  document.getElementById('confirmBtn').addEventListener('click',function(){
    closeSheet();
    var panel=document.getElementById('chargingPanel');
    panel.hidden=false;
    panel.scrollIntoView({behavior:'smooth',block:'center'});
    toast.textContent='充电已启动，实时功率 60.2kW…';
  });
  document.getElementById('stopBtn').addEventListener('click',function(){
    document.getElementById('chargingPanel').hidden=true;
    showToast('已停止充电，本次费用 ¥24.50 已自动扣款…');
  });

  // energy pack
  var packPrice={'100':'¥98','200':'¥188','300':'¥268'};
  document.querySelectorAll('.pack-option').forEach(function(o){
    o.addEventListener('click',function(){
      document.querySelectorAll('.pack-option').forEach(function(x){x.classList.remove('active');x.setAttribute('aria-checked','false');});
      o.classList.add('active');o.setAttribute('aria-checked','true');
      document.querySelector('.pack-options').setAttribute('aria-activedescendant','');
      document.querySelector('.pack-foot .price').textContent=packPrice[o.dataset.kwh];
    });
  });

  // empty state demo
  document.getElementById('expandBtn').addEventListener('click',function(){
    document.getElementById('emptyState').hidden=true;
    document.getElementById('stationList').style.display='';
    showToast('已扩大搜索范围至 10km…');
  });
})();
