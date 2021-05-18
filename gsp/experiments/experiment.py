import pandas as pd

def save_experiment_to_csv(data_, experiment_name, path_):
	results_df = pd.DataFrame(data=data_, columns=['Seq','Sup'])
	results_df.to_csv(path_or_buf=path_+'gsp_results_'+experiment_name+'.csv',index=False)
	print('Results saved to csv')