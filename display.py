import pandas as pd

def highlight_cell(x):
  sodu_style = x.style.set_properties(**{
      "border" : "1px solid black",
      "text-align" : "center",
      "padding" : "10px"
  })

  subset_rows = ['R2','R4','R6']
  subset_cols = ['C3','C6']
  sodu_style = sodu_style.set_properties(subset=(subset_rows,slice(None)),**{
      "border-bottom" : "3px solid black",
  })
  sodu_style = sodu_style.set_properties(subset=(slice(None),subset_cols),**{
      "border-right" : "3px solid black",
  })
  sodu_style = sodu_style.set_properties(subset=(slice(None), ['C1']),
                                        **{"border-left" : "3px solid black"
                                        })
  sodu_style = sodu_style.set_properties(subset=(['R1'], slice(None)),
  **{
      "border-top" : "3px solid black"
  })
  return sodu_style   
