DEV data for SemEval-2013 Task #2: Sentiment Analysis on Twitter

Task organizers:
Theresa Wilson   Johns Hopkins University, HLTCOE
Zornitsa Kozareva  University of Southern California, ISI
Preslav Nakov  Qatar Computing Research Institute, Qatar Foundation
Sara Rosenthal  Columbia University
Veselin Stoyanov Johns Hopkins University 
Alan Ritter  University of Washington

This data is released under a Creative Commons Attribution 3.0 Unported License (http://creativecommons.org/licenses/by/3.0/). 

Please note that by downloading the Twitter data you agree to abide by the Twitter terms of service (https://twitter.com/tos), and in particular you agree not to redistribute the data and to delete tweets that are marked deleted in the future. You MUST NOT re-distribute the tweets, the annotations or the corpus obtained, as this violates the Twitter Terms of Use.

Version 1.0: March 6, 2013.


NOTE

The development data has already been released as Twitter IDs: http://www.cs.york.ac.uk/semeval-2013/task2/index.php?id=data
Here we release it in a different format that is ready for the scorer to use; this is also the format for the test data.


DIRECTORY CONTENT

twitter-dev-input-A.tsv -- dev input for task A, Twitter messages
twitter-dev-gold-A.tsv  -- gold lables for twitter-dev-input-A.tsv
twitter-dev-full-A.tsv  -- full version of the dev input for task A, Twitter messages (see "objective" below)

twitter-dev-input-B.tsv -- dev input for task B, Twitter messages
twitter-dev-gold-B.tsv  -- gold lables for twitter-dev-input-B.tsv
twitter-dev-full-B.tsv  -- full version of the dev input for task B, Twitter messages (see "objective" below)



FORMATS

-----------------------TASK A-----------------------------------------
--INPUT--
id1<TAB>id2<TAB>start_token<TAB>end_token<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101        2       2       unknwn  amoure wins oscar
NA      15115101        3       4       unknwn  who's a master brogramer now?

--Gold Standard--
The gold standard following the same format as the system output above 

-----------------------TASK B-----------------------------------------
(Task B uses the same format as Task A, but it excludes the start and end token fields.)
--INPUT--
id1<TAB>id2<TAB>unknwn<TAB>tweet_text

for example:
NA      15115101       unknwn  amoure wins oscar
NA      15115101       unknwn  who's a master brogramer now?

--Gold Standard--
The gold standard following the same format as the system output above 



See also the scorer and its README.

EVALUATION

The evaluation metric is average F-measure (averaged F-positive and F-negative, and ignoring F-neutral; note that this does not make the task binary!), as well as F-measure for each class (positive, negative, neutral), which can be illuminating when comparing the performance of different systems.

See also the scorer for details on scoring the output.


DATASET USE

The development dataset is intended to be used as a development-time evaluation dataset as the participants develop their systems. However, the participants are free to use the dataset in any way they like, e.g., they can add it to their training dataset as well.


ABOUT "OBJECTIVE"

Some of the datasets (e.g., the training dataset) contain "objective" labels, which the participants are free to use on training as they wish. However, we recommend that for task A these labels be ignored since there are no "objective" labels in the testing dataset. For task B, "objective" and "neutral" labels should be merged into "neutral"; the two labels are merged likewise for the test dataset. So, at test time, for both task A and task B, the systems have to predict just three labels: positive, negative and neutral. However, while for task A neutral means just "neutral", for task B, neutral means "neutral OR objective".

NOTE: These updates related to objectives are already done in this release (input & gold): (i) objectives are removed from task A, and (ii) objective and neutral are merged into neutral for task B.
We also provide the original (full) version.


USEFUL LINKS:

Google group: semevaltweet-2013@googlegroups.com
Task website: http://www.cs.york.ac.uk/semeval-2013/task2/
SemEval-2013 website: http://www.cs.york.ac.uk/semeval-2013/


NOTE: You can cite the folowing paper when referring to the dataset:

	SemEval'2013: SemEval-2013 Task 2: Sentiment Analysis in Twitter.
	Preslav Nakov, Sara Rosenthal, Zornitsa Kozareva,
	Veselin Stoyanov, Alan Ritter, Theresa Wilson
	http://www.aclweb.org/anthology/S/S13/S13-2052.pdf	


LICENSE

The accompanying dataset is released under a Creative Commons Attribution 3.0 Unported License
(http://creativecommons.org/licenses/by/3.0/).
