class ProcessModel:
    def __init__(self,item,region,line,groupmark,stationcode,stationname,retestrate,
                 linedownrate,efficiency,manualct,machinect,stationct,piece,hcpermachine,hc,targetuph,remark):
        self.item=item
        self.region=region
        self.line=line
        self.groupmark=groupmark
        self.stationcode=stationcode
        self.stationname=stationname
        self.retestrate=retestrate
        self.linedownrate=linedownrate
        self.efficiency=efficiency
        self.manualct=manualct
        self.machinect=machinect
        self.stationct=stationct
        self.piece=piece
        self.hcpermachine=hcpermachine
        self.hc=hc
        self.targetuph=targetuph
        self.remark=remark













"""
        item int primary key auto_increment,
        region varchar(10) not null,
        line varchar(20) not null,
        groupmark varchar(30) not null,
        stationcode varchar(50) not null,
        stationname varchar(80) not null,
        retestrate float not null default 0.0 ,
        linedownrate float not null default 0.0,
        efficiency decimal(3,2) not null default 0.92,
        manualct float not null,
        machinect float not null,
        stationct float,
        piece int not null default 1,
        hcpermachine int not null default 1,
        hc float,qpl float,
        targetuph int not null,
        remark text);
"""