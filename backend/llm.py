import openai, json, os, ast
import json
import os
from dotenv import load_dotenv

# Set up API key

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def parseResponse(responseString:str):
    responseString = responseString.replace('\n', '')

    formattingException = Exception("Response is not well formatted")
    formattingException.add_note(responseString)

    if responseString[0] == '{' and responseString[-1] == '}':
        resultDict = json.loads(responseString)
    else:
        raise formattingException
    
    return resultDict


def generateStudyGuide(data,):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", 
            "content": '''can you generate a study guide to review the content from this transcription, please respond in this json format only:{"study_guide":[{"main point":"", "subpoints":["2-3 brief","subpoints","in few words"], "explanation":"helpful description containing several sentences"}]}. Please do not include labels beyond the minimum required for a json (i.e. do not have any writing or code before the json file) \n''' + data
            }
        ]
    )

    try:
        responseArray = parseResponse(response.choices[0].message.content)
    except Exception as e:
        raise e
        
    return responseArray


def generateFlashcards(data):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", 
            "content": '''can you generate flash cards for the main ideas included in this transcription, please respond in this json format only:{"flashcards":[{"term/concept":"","explanation":":""}]}. Please do not include labels beyond the minimum required for a json (i.e. do not have any writing or code before the json file) \n''' + data
            }
        ]
    )

    try:
        responseArray = parseResponse(response.choices[0].message.content)
    except Exception as e:
        raise e
        
    return responseArray
    

def generateQuiz(data):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", 
            "content": '''can you generate multiple choice and true/false quiz questions with answers from this transcription, please respond in this json format only:{"quiz":[{"question":"", "choices":["a":"", "b":"","c":"","d":""], "answer":""}]}. Please do not include labels beyond the minimum required for a json (i.e. do not have any writing or code before the json file) \n''' + data
            }
        ]
    )

    try:
        responseArray = parseResponse(response.choices[0].message.content)
    except Exception as e:
        raise e
        
    return responseArray


testData = '''00:00:00.000 This video is about learning styles.
00:00:01.987 What kind of learner are you?
00:00:03.950 Oh yeah, I'm a visual person
00:00:05.060 so I have to see things, yeah.- Oh yeah, same.
00:00:05.893 I think visual learner.
00:00:07.630 Visual.
00:00:08.463 I mean, like, I rememberformulas like auditory.
00:00:11.040 I need to be like,interacting with the material.
00:00:13.260 I like to learn by doing it myself.
00:00:15.010 Very hands-on.
00:00:15.843 Hands-on learner.
00:00:16.820 Hands-on?
00:00:17.653 So like, if I have a model,I'd like to look at that
00:00:19.480 and look it over.
00:00:20.430 Part of this video wassponsored by Google Search.
00:00:25.040 There is this idea ineducation that everyone
00:00:27.510 has their own preferred way of learning,
00:00:29.210 their so-called learning style.
00:00:31.160 If information is presented in accordance
00:00:32.840 with the learning style, well,then they'll learn better.
00:00:36.090 Now, there are dozens ofdifferent learning style theories,
00:00:38.950 but the most common one identifies
00:00:40.660 four main learningstyles, visual, auditory,
00:00:43.790 reading-writing, andkinesthetic or VARK for short.
00:00:47.132 Visual learners learn best from images,
00:00:49.570 demonstrations, and pictures.
00:00:51.560 People may say things, butI can't really take it in.
00:00:54.110 I just gotta see 'em act itout or write it or something.
00:00:57.830 [Derek] Auditory learners learn best
00:00:59.230 from listening to an explanation.
00:01:01.240 Like in school, I wasalways engaged in the lecture
00:01:04.410 and that was usually goodenough to pass a test.
00:01:07.300 [Derek] Reading-writinglearners learn best
00:01:08.900 from reading and writing.
00:01:10.100 Like I can get pretty much anything
00:01:11.980 out of reading a textbook or something.
00:01:13.610 [Derek] And kinestheticlearners learn best by doing.
00:01:16.010 Physically interacting with the world.
00:01:17.740 Hands-on.
00:01:18.573 You have to touch things,you have to play with things,
00:01:20.500 you know, it's a contact sport.
00:01:23.065 You have to do it yourself.
00:01:24.550 I want to try somethingwith you, a little experiment.
00:01:27.530 I want to show you 10 pictures of things
00:01:29.067 and I don't want you to say anything
00:01:30.810 while you're looking at them,and at the end of the 10
00:01:32.910 you tell me how many you can remember.
00:01:34.660 Okay.
00:01:35.493 Okay?- Okay.
00:01:36.326 Okay.
00:01:38.910 Now, learning stylesmake intuitive sense
00:01:40.900 because we know everyone is different.
00:01:43.510 Some people have better spacial reasoning.
00:01:45.960 Others have betterlistening comprehension.
00:01:48.580 We know some people are better readers
00:01:50.210 while others are good with their hands.
00:01:52.540 It's sort of very muchfits with a broad strain
00:01:56.430 of thought in the recentWestern tradition is,
00:02:00.180 we're all unique, we're all different.
00:02:01.850 And so you don't want to say, like,
00:02:02.800 everybody learns the same way.
00:02:04.157 That sort of conflicts with our feelings
00:02:07.090 about what it means to be human.
00:02:09.190 So doesn't it make sensethat people should learn better
00:02:12.190 in their own preferred learning style?
00:02:14.390 Well, teachers certainly seem to think so.
00:02:16.720 A survey of nearly 400teachers from the UK
00:02:19.410 and the Netherlands foundthat over 90% believed
00:02:22.550 that individuals learn betterwhen they receive information
00:02:25.510 in their preferred learning style.
00:02:27.340 [Instructor] Just like every professor
00:02:28.440 has a different style of teaching,
00:02:30.000 you have a different style of learning.
00:02:31.840 [Instructor] But when histeacher starts using visuals,
00:02:34.000 Johnathan finds it easier to focus
00:02:35.620 and understand the material
00:02:36.910 so he might be a visual learner.
00:02:39.382 [Derek] Can you tell mewhat that means to you?
00:02:41.610 Like, what does it meanto be a visual learner?
00:02:43.360 To me it means thatfor me to learn something
00:02:45.620 sometimes you need to drawit or I need to write it down
00:02:48.250 or I need to see a picture or a movie.
00:02:51.080 For example, scienceclasses, I get bored easily
00:02:54.200 just listening and I thinkit's more interesting for me
00:02:57.320 to actually be able to do it.
00:02:59.140 [Derek] How do you knowthat you're a visual learner?
00:03:00.750 I don't, I just assumed.
00:03:03.380 To take advantage of learning styles
00:03:05.130 then teachers need to do two things.
00:03:07.520 First, identify the learning style
00:03:09.780 of each of their students.
00:03:11.120 And second, teach each student
00:03:13.330 in accordance with their learning style.
00:03:15.550 On the VARK website it says,once you know about VARK,
00:03:19.120 its power to explain thingswill be a revelation.
00:03:22.720 But before you take anonline learning styles quiz,
00:03:25.310 it's a good idea to ask, dolearning styles even exist?
00:03:29.060 I mean, do you have one?
00:03:30.260 And if you're taughtin accordance with it,
00:03:32.380 would you learn better?(warm instrumental music)
00:03:35.320 Well, you could test this
00:03:36.225 by running a randomized control trial
00:03:38.363 where first you would identify learners
00:03:40.620 with at least twodifferent learning styles,
00:03:42.440 say visual and auditory andthen randomly assign learners
00:03:46.460 to one of two educational presentations,
00:03:48.840 one visual, one auditory.
00:03:50.870 So for half of the students
00:03:52.420 the experience will matchtheir learning style
00:03:54.700 and for the other half it won't.
00:03:57.000 And then you give everyone the same test.
00:03:59.930 If the learning stylehypothesis is correct,
00:04:02.350 the results should show better performance
00:04:04.270 when the presentationmatches the learning style
00:04:07.000 than when they're mismatched.
00:04:09.830 I tried a very unscientific version
00:04:12.150 of this experiment on the street.
00:04:14.090 For some people, I matchedtheir learning style
00:04:16.637 so I showed visual learnerspictures of 10 items,
00:04:21.149 but for other visual learnersI read out the items instead.
00:04:25.819 Bell, penguin, sun.
00:04:29.810 Okay, I'm maxed out.
00:04:30.780 [Derek] How many can you remember?
00:04:32.033 I don't know.
00:04:32.866 Hair, knife, duck, heart, butterfly.
00:04:38.800 Apple, bicycle, guitar.
00:04:42.230 There was a spider.
00:04:44.240 Did I say eye already?
00:04:45.400 Trumpet, pear.- Pear.
00:04:47.040 Butterfly.- Duck.
00:04:48.340 Knife.- Boat.
00:04:49.350 Heart.- Knife.
00:04:50.200 Heart.
00:04:51.033 I couldn't tell you therest, that's all I got.
00:04:53.390 [Derek] Most people could remember
00:04:54.840 only about five or six things.
00:04:56.897 Yeah, yeah.- Six, six is not bad.
00:04:58.227 All right.
00:04:59.060 Six.- Six out of 10
00:05:00.420 which is not bad, right?- Oh, all right, yeah.
00:05:02.007 That's a passing score.
00:05:03.170 Candle.- Oh.
00:05:04.003 Candle.- Everyone forgets the candle.
00:05:05.475 But a few could remembersubstantially more,
00:05:08.540 say, eight or nine items.
00:05:10.380 Bug, I don't know if I said bug.
00:05:12.432 Guitar, bike, eye,bell, spoon, sun, chair.
00:05:17.450 I'm forgetting the last two.
00:05:18.710 That's pretty good.- Eight is really good.
00:05:20.270 Oh, cool.
00:05:21.103 Nine?- Nine out of 10.
00:05:22.050 Nine, very impressive.
00:05:24.900 But the reason didn't seem tobe because the presentation
00:05:27.510 matched their preferred learning style
00:05:29.930 but because they employeda memory strategy.
00:05:33.112 So as you were showing I wasmaking an order in my head.
00:05:36.047 So as I saw more I wouldjust add it to the list
00:05:39.250 and I was repeating the listas I was looking at them
00:05:41.240 so I could just say it out loud.
00:05:42.600 Did you try a strategywhile you were looking
00:05:44.788 at those pictures?- Yeah, yeah.
00:05:46.580 So I guess I tried creating a story
00:05:49.263 'cause it's easier to remember a story
00:05:50.780 than just individual objects.
00:05:52.660 So I tried to tie it all into one story.
00:05:55.190 This is all obviouslyanecdotal evidence,
00:05:57.370 but rigorous studieslike the one I outlined
00:05:59.810 have been conducted.
00:06:01.220 For example, one looked atvisualizers versus verbalizers
00:06:04.790 instead of visual versusauditory learners.
00:06:06.966 The study was computer-based,
00:06:09.600 so first students' learningstyles were assessed
00:06:11.870 using questions like, wouldyou rather read a paragraph
00:06:15.020 or see a diagram describing an atom?
00:06:17.440 The researchers also providedsome challenging explanations
00:06:20.520 with two buttons, visualhelp or verbal help.
00:06:24.110 The visual one played a short animation
00:06:26.290 whereas the verbal helpgave a written explanation.
00:06:29.670 From these measures combined,the researchers categorized
00:06:32.100 the students as eithervisualizers or verbalizers
00:06:35.280 and then the studentswere randomly assigned
00:06:37.470 to go through a text-based
00:06:39.090 or picture-based lesson on electronics.
00:06:42.220 When a student hoveredtheir mouse over key words
00:06:44.460 in the lesson in the text-based group,
00:06:46.560 a definition and clarification came up.
00:06:48.810 But in the picture group,
00:06:50.130 an annotated diagram was shown instead.
00:06:52.780 And after the lesson,the students did a test
00:06:55.100 to assess their learning.
00:06:56.710 The students whosepreferred learning style
00:06:58.470 matched their instructionperformed no better on the tests
00:07:02.560 than those whoseinstruction was mismatched.
00:07:05.200 The researchers ran the test again
00:07:06.810 with 61 non-college-educated adults
00:07:09.250 and found exactly the same result.
00:07:11.364 But learning styles are a preference
00:07:13.886 so how strongly do learnersstick to their preference?
00:07:17.710 Well, in a 2018 study duringthe first week of semester,
00:07:20.630 over 400 students at auniversity in Indiana
00:07:23.440 completed the VARK questionnaireand they were classified
00:07:26.480 according to their learning style.
00:07:28.100 Then at the end of the semester
00:07:29.320 the same students completed astudy strategy questionnaire.
00:07:32.374 So how did they actuallystudy during the term?
00:07:35.780 Well, an overwhelming majority of students
00:07:37.709 used study strategies whichwere supposedly incompatible
00:07:40.681 with their learning style,
00:07:42.580 and the minority of students who did
00:07:44.118 did not perform significantly differently
00:07:46.370 on the assessments in the course.
00:07:48.553 The visual auditoryreading-writing, kinesthetic
00:07:51.120 or VARK model cameabout from Neil Fleming,
00:07:53.920 a school inspector in New Zealand.
00:07:56.040 Describing the origins of VARK he says,
00:07:58.390 I was puzzled when Iobserved excellent teachers
00:08:00.540 who did not reach some learnersand poor teachers who did.
00:08:04.220 I decided to try to solve this puzzle.
00:08:06.360 There are, of course, manyreasons for what I observed.
00:08:09.540 But one topic that seemedto hold some magic,
00:08:12.500 some explanatory power,
00:08:14.150 was preferred modes oflearning, modal preferences.
00:08:17.850 And thus, VARK was born.
00:08:20.240 There was no study that revealed
00:08:22.020 students naturally clusterinto four distinct groups.
00:08:24.980 Just some magic that might explain
00:08:26.720 why some teachers can reachstudents while others can't.
00:08:29.930 But how can this be?
00:08:31.430 If we accept that somepeople are more skilled
00:08:33.650 at interpreting and rememberingcertain kinds of stimuli
00:08:35.960 than others like visual or auditory,
00:08:38.659 then why don't we seedifferences in learning
00:08:41.179 or recall with different presentations?
00:08:43.600 Well, it's because what weactually want people to recall
00:08:46.480 is not the precise nature of the images
00:08:48.810 or the pitch or quality of the sound.
00:08:51.010 It's the meaning behind the presentations.
00:08:53.212 There are some tasks thatobviously require the use
00:08:55.890 of a particular modality.
00:08:57.520 Learning about music, for example,
00:08:59.130 should have an auditory component.
00:09:01.180 Similarly, learning about geography
00:09:02.910 will involve looking at maps.
00:09:05.055 And some people will have greater aptitude
00:09:07.540 to learn one task over another.
00:09:09.310 Someone with perfect pitch, for example,
00:09:11.090 will be better able to recallcertain tones in music.
00:09:13.830 Someone with excellentvisual-spatial reasoning
00:09:15.820 will be better at learning the locations
00:09:17.460 of countries on a map.
00:09:18.870 But the claim of learning style theories
00:09:20.730 is that these preferences
00:09:21.990 will be consistentacross learning domains.
00:09:24.792 The person with perfect pitch
00:09:26.870 should learn everything better auditorily
00:09:29.157 but that is clearly not the case.
00:09:31.780 Most people will learngeography better with a map.
00:09:35.940 Review articles of learningstyles consistently conclude
00:09:38.910 there is no credible evidencethat learning styles exist.
00:09:43.030 In a 2009 review, theresearchers note, the contrast
00:09:46.360 between the enormous popularity
00:09:48.100 of the learning stylesapproach within education
00:09:50.630 and the lack of credibleevidence for its utility is,
00:09:54.060 in our opinion, striking and disturbing.
00:09:57.250 If classification ofstudents' learning styles
00:09:59.080 has practical utility, itremains to be demonstrated.
00:10:02.870 What we're expecting is,if your style was honored
00:10:06.210 you're going to perform better than if
00:10:08.320 you had some experience thatconflicted with your style.
00:10:10.880 And this is where we don't see any support
00:10:13.710 for the learning styles theory.
00:10:15.730 One of the reasons manypeople find learning styles
00:10:17.581 so convincing is because theyalready believe it to be true.
00:10:21.720 For example, they might already think
00:10:23.288 that they're a visual learner,and then when a teacher
00:10:26.060 shows them a diagram of, say, a bike pump
00:10:29.000 and suddenly the concept clicks,
00:10:30.920 well, they interpret this as evidence
00:10:32.660 for their visual learning style.
00:10:34.310 You already believe thatlearning styles is right.
00:10:36.810 When you have an experiencethe first think you think is,
00:10:39.600 is that in some way consistentwith learning styles?
00:10:42.260 And if it is, you don't think further.
00:10:43.830 When in reality that diagrammight just be a great diagram
00:10:47.250 that would have helped anyone learn.
00:10:49.240 When we already believe theworld to be a certain way,
00:10:52.230 then we interpret new experiencesto fit with those beliefs
00:10:55.690 whether they actually do or not.
00:10:57.908 So if learning styles
00:10:59.610 don't improve learning, then what does?
00:11:02.440 Well, there's a large body of literature
00:11:03.720 that supports the claimthat everyone learns better
00:11:05.980 with multimodal approaches
00:11:07.330 where words and picturesare presented together
00:11:09.980 rather than eitherwords or pictures alone.
00:11:12.600 Now there's gonna be wordsas well as the picture.
00:11:15.090 We're gonna see if this is any better.
00:11:17.060 This is known as the multimedia effect,
00:11:19.500 and it explains in part, at least,
00:11:21.430 why videos can be suchpowerful tools for learning
00:11:24.220 when the narrationcomplements the visuals.
00:11:26.920 Duck.- Duck.
00:11:30.134 Heart.- Heart.
00:11:31.720 [Derek] In my PhD research,I found explicit discussion
00:11:34.440 of misconceptions was essential
00:11:36.140 in multimedia teachingfor introductory physics.
00:11:38.830 How many is that?- Six.
00:11:40.050 Six, okay, that's good.
00:11:41.030 That is a whole 50% better.
00:11:43.490 Do you think that was easier?
00:11:44.948 Yeah, yeah, 100%, 100%.- Yeah, with the words, yeah.
00:11:47.980 Ultimately, the mostimportant thing for learning
00:11:50.214 is not the way theinformation is presented
00:11:52.980 but what is happeninginside the learner's head.
00:11:55.990 People learn best whenthey're actively thinking
00:11:58.310 about the material, solving problems
00:12:00.450 or imagining what happens ifdifferent variables change.
00:12:04.010 I talked about how and why we learn best
00:12:06.290 in my video, "The Science ofThinking" so check that out.
00:12:09.690 Now, the truth is, thereare many evidence-based
00:12:11.960 teaching methods that improve learning.
00:12:14.220 Learning styles is just not one of them.
00:12:17.810 And it is likely, given the prevalence
00:12:20.210 of the learning styles misconception
00:12:21.830 that it actually makes learning worse.
00:12:24.210 I mean, learning styles giveteachers unnecessary things
00:12:27.130 to worry about, and theymake some students reluctant
00:12:29.640 to engage with certaintypes of instruction.
00:12:32.650 And all the time and moneyspent on learning styles
00:12:35.220 and related training could bebetter spent on interventions
00:12:37.720 that actually improve learning.
00:12:40.180 You are not a visual learnernor an auditory learner
00:12:44.080 nor a kinesthetic learner,or more accurately,
00:12:47.130 you are all these kinds of learner in one.
00:12:50.400 The best learning experiences are those
00:12:52.470 that involve multiple different ways
00:12:54.318 of understanding the same thing.
00:12:56.620 And best of all, this strategy works
00:12:58.610 not just for one subset ofpeople but for everyone.
00:13:03.435 (radio tuner chirping)
00:13:07.470 This part of the video wassponsored by Google Search.
00:13:10.160 Now, there are lots of topics out there
00:13:11.730 that are controversial likelearning styles, for example.
00:13:14.960 Most people believelearning styles are a thing
00:13:17.690 whereas educational researchers
00:13:19.270 find no robust evidence for them.
00:13:21.400 And if you search for learning styles,
00:13:23.279 you'll get lots of siteswith resources and quizzes.
00:13:26.520 But if you search forlearning styles debunked,
00:13:29.130 well, then you'll find articles
00:13:30.810 about how there is very little evidence
00:13:32.630 for the learning styles hypothesis.
00:13:34.630 I think one of the mostcommon traps people fall into
00:13:37.475 is only searching for information
00:13:39.470 that confirms what they already believe.
00:13:41.750 A common mistake is puttingthe answer you're looking for
00:13:44.420 right in the search query.
00:13:46.140 A better idea is to try another search,
00:13:48.620 adding debunked or false atthe end and see what comes up.
00:13:51.510 And Google makes iteasy to get more detail
00:13:53.630 about the source of the information.
00:13:55.570 Just click the three dotsnext to any search result
00:13:58.250 and then you can judge for yourself
00:13:59.880 whether the information is trustworthy
00:14:01.540 and if you want to visit the site.
00:14:02.910 A Google Search is meant to surface
00:14:04.510 the most relevantinformation for your query.
00:14:07.360 But it's up to you toformulate that query,
00:14:10.160 try a few different searches,
00:14:11.530 and assess whether theinformation is reliable.
00:14:14.570 And the whole point of Veritasiumis to get to the truth.
00:14:17.300 So I'm excited to encourage everyone
00:14:18.850 to think more criticallyabout how we get information.
00:14:22.070 I want to thank Google forsponsoring this part of the video
00:14:24.360 and I want to thank you for watching.'''

print(str(generateStudyGuide(testData)).replace("\'", "\"")) # Testing line only

