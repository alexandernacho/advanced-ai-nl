// Gedeelde grafiekbediening voor een bestaande werkmap en toekomstige imports.
export function readSelection(sheet){
 if(sheet.getRange('A7').values[0][0]==='Jaar')return {
  type:sheet.getRange('B6').values[0][0],year:Number(sheet.getRange('B7').values[0][0]),quarter:sheet.getRange('B8').values[0][0]
 };
 const serial=sheet.getRange('B10').values[0][0];
 const date=typeof serial==='number'?new Date(Date.UTC(1899,11,30)+serial*86400000):new Date();
 return {type:'Kwartaal',year:date.getUTCFullYear(),quarter:`Q${Math.floor(date.getUTCMonth()/3)+1}`};
}

export function applyQuarterControls(wb,{selection,years,recordCount=0}={}){
 const s=wb.worksheets.getItem('Grafieken');
 selection=selection||readSelection(s);
 years=years||[selection.year-1,selection.year,selection.year+1,selection.year+2,selection.year+3,selection.year+4,selection.year+5];
 s.getRange('A5:B11').clear({applyTo:'contents'});
 s.getRange('A5:B11').format.fill='#FFFFFF';
 s.getRange('B5:B11').dataValidation={rule:{type:'none'},inCellDropDown:false};
 s.getRange('A5:B8').values=[['Weergavevaluta','USD'],['FCF-periodetype',selection.type],['Jaar',selection.year],['Kwartaal',selection.quarter]];
 s.getRange('B7:B8').setNumberFormat('General');
 s.getRange('B6:B8').format.fill='#FFF1CC';
 s.getRange('B6').dataValidation={rule:{type:'list',values:['Kwartaal','Halfjaar','Negen maanden','Jaar']},inCellDropDown:true};
 s.getRange('B7').dataValidation={rule:{type:'list',values:[...new Set(years)].sort((a,b)=>a-b).map(String)},inCellDropDown:true};
 s.getRange('B8').dataValidation={rule:{type:'list',values:['Q1','Q2','Q3','Q4']},inCellDropDown:true};
 s.getRange('E5:F8').clear({applyTo:'contents'});
 s.getRange('A10').values=[['Jaar = kalenderjaar van de einddatum. Q1–Q4 = kwartaal volgens het rapport.']];
 s.getRange('A11').values=[['Zonder kwartaalvermelding gebruikt Excel het kalenderkwartaal van de einddatum.']];
 s.getRange('H5').values=[['Werkelijke periodes en officieel boekjaar staan in Historiek.']];
 const end=Math.max(2005,recordCount+5),range=c=>`'Historiek'!$${c}$6:$${c}$${end}`;
 const startYear='DATE($B$7,1,1)', nextYear='DATE($B$7+1,1,1)';
 const quarterStart='DATE($B$7,(VALUE(RIGHT($B$8,1))-1)*3+1,1)';
 const quarterEnd='DATE($B$7,VALUE(RIGHT($B$8,1))*3+1,1)';
 for(let r=49;r<=58;r++)for(const [col,metric,type]of[
  ['B','FCF','$B$6'], ['C','Schuld','"Peildatum"'], ['D','Omzetgroei','"Kwartaal"']
 ]){
  const criteria=`${range('B')},$A${r},${range('C')},"${metric}",${range('F')},${type},${range('G')},"<>"`;
  const reported=`${criteria},${range('T')},$B$8,${range('E')},">="&${startYear},${range('E')},"<"&${nextYear}`;
  const fallback=`${criteria},${range('T')},"",${range('E')},">="&${quarterStart},${range('E')},"<"&${quarterEnd}`;
  const count=`COUNTIFS(${reported})`, fallbackCount=`COUNTIFS(${fallback})`;
  const sum=args=>`SUMIFS(${range('S')},${args})`;
  s.getRange(`${col}${r}`).formulas=[[`=IF(${count}=1,${sum(reported)},IF(AND(${count}=0,${fallbackCount}=1),${sum(fallback)},NA()))`]];
 }
 return selection;
}
