clc
clear

data = load ('-ascii', 'pmts_target.txt');
data2 = load ('-ascii', '../s_output/Sim_100k_063.txt');

hist(sum(data2'), 100)
xlim([0 4000])
title('Histograma de hits')

figure
hist(sum(data'), 60)
xlim([1 4000])
title('Histograma de hits')