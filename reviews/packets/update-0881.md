<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0881.txt",
      "sha256": "45547c2e89944a6498313dbae418b9c5d8cfb37a241c6afcf190b2566a3808b2",
      "bytes": 12772
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "806879bff747897875de8dc4e9d240e705b67e2d9a0c69a355742b4506e112fc",
      "bytes": 1959
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "effe85ae8155687361af6fa50a69ec256e5823559355bc134b1226fd78b6e35d",
      "bytes": 759
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "4bb6e400ebcdb26d0940a2221bfee5091869fd1f250e0070e4f503001bdb7a4f",
      "bytes": 765
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "05421f09c1602e4bf1e02b590939422de09eb2ac33e367444bb73132b360984c",
      "bytes": 258643
    }
  ],
  "estimated_tokens": 8635
}
-->

# Durable State Update — Chapter 881

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 881. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 881. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 881,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 881,
    "continuity_sources": [881],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Emperor has confirmed the rumors about Prince Shangshan’s return and the existence of an heir; whether Aehyang is pregnant remains unconfirmed.",
    "The Emperor plans a banquet attended by Shangshan and the civil and military officials; Hong Jin suspects it could be a trap.",
    "Ma Sanbao spread the rumors using information Jin Taekyung gave him; the Emperor ordered the arrested rumor-spreaders released.",
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents and the invitation’s purpose remain unknown."
  ],
  "continuity_sources": [
    879,
    880
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet be used to harm Shangshan or eliminate dissidents?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Will the Myriad-Poison Ring protect Shangshan from Blood Soul Gu?"
  ],
  "safe_through": 880,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 동량지재 | **pillar of Huashan** | Reputation attributed to Baek Museong. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 축골공 | **Bone-Shrinking Technique** | A martial art that stretches and shrinks bone and flesh to alter the user's appearance. |
| 역천 | **defying heaven** | Supernatural power that regenerates the masked man's body. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 879
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 880
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

## Korean source

```text
＃881화



예로부터 밤말은 쥐가 듣고, 낮말은 새가 듣는다고 했다.

그러나 누군가의 초대를 받아 이른 아침부터 밀실에 모여 앉은 손님들은 그런 케케묵은 격언 따위에 조금도 흔들리지 않았다.

쥐는 밟아 죽이면 되고, 새는 쏘아 맞히면 그만이다.

그들이 유일하게 신경 쓰는 존재는 금의위(錦衣衛)뿐이었다.

황제의 번견(番犬)이나 다름없는 금의위들은 누렁이의 싯누런 털을 닮은 황금빛 갑옷을 걸치고 사방을 이 잡듯이 뒤지는 것이 특기였다.

표적의 냄새를 맡고, 추적하고, 그 목덜미에 악취 나는 이빨을 박아넣은 후 제 주인에게 달려가 꼬리를 흔드는 것이다.

더군다나 황도에는 수많은 이목(耳目)이 존재하는 만큼, 제아무리 극비리에 움직였다 해도 목에 걸린 가시처럼 신경 쓰이는 것은 어쩔 수 없었다.

아마도 그래서였을까.

십여 명이 한자리에 모여 있음에도 밀실 안에는 한동안 불편한 침묵만이 감돌았다.

어느 순간, 미세한 소음과 함께 그들이 기다리던 마지막 한 사람이 모습을 드러내기 전까지는.

끼익.

머리 위를 덮고 있던 낡은 가림판이 열리고 흐릿한 빛이 쏟아진다. 어둠에 익숙해져 있던 이들은 반사적으로 눈살을 찌푸리면서도 긴장의 끈을 놓지 않았다.

지금 막 밀실로 발을 디딘 저 낯선 사내가, 자신들이 익히 아는 그 아군인지 확신이 서지 않았으니까.

그리고 새롭게 등장한 사내는 즉각 그 눈동자들에 담긴 뜻을 이해했다.

“아, 이런 실례를. 급히 오느라 잠시 잊었습니다.”

꾸득, 우드득.

“음.”

누가 먼저랄 것도 없이 동시에 흘러나오는 침음성. 십여 명의 손님들은 가라앉은 눈빛으로 사내를 둘러싼 변화를 지켜보았다.

스륵.

마치 파도처럼 일그러지는 이목구비.

길쭉하던 인중이 짧아지고, 유독 눈에 띄던 주먹코는 날렵해졌으며 흐릿하게 풀려 있던 눈동자에는 기이한 정광(正光)이 깃들었다.

이것만으로도 충분히 놀랄 만한 일인데, 변화는 거기에서 끝나지 않았다.

뿌드득.

수백 조각의 뼈가 어긋나는 소리와 함께 줄어들었다 늘어났다를 반복하는 신체.

이와 같은 변화는 순식간에 일어났고, 찰나라고 부를 만한 시간이 흐르자 조금 전 보았던 사내의 흔적은 그 어디에서도 찾아볼 수 없었다.

그 빈 자리를 메운 것은 호리호리한 체구를 지닌 삼, 사십 대의 미남자뿐.

마침내 익숙한 얼굴을 마주하게 된 손님들은 그제야 팽팽하게 당겨진 긴장의 끈을 풀었다.

“언제봐도 신묘한 기예(技藝)로군.”

“이만하면 익숙해질 때도 되었는데, 하나같이 매번 긴장하게 되는 것을 보면 마 태감의 재주가 참으로 놀랍소.”

곳곳에서 흘러나오는 감탄 섞인 말에, 동창 병필태감 마삼보는 빙긋 웃었다.

“그저 어쩌다 보니 익히게 된 잡기(雜技)일 뿐입니다.”

신기에 가까운 역용술과 축골공을 겸손한 어투로 일축한 마삼보가 말을 이었다.

“그보다 모두 약속된 시각에 모이셨군요. 오시는 길이 불편하지는 않으셨는지 모르겠습니다.”

손님들이 여유를 되찾은 목소리로 대답했다.

“생각보다는 그리 나쁘진 않았소. 마 태감의 충복들이 도와주기도 했고, 위장도 훨씬 철저하게 했으니.”

“물론 이 흉측한 물건이 심히 불쾌하면서도 갑갑하긴 하지만, 금의위 놈들의 감시를 피할 수 있다면 뭔들 못하겠소?”

누군가가 자신의 안면 위에 덧씌운 인피면구(人皮面具)를 가리키며 말하자, 모두가 공감하듯 고개를 끄덕였다.

맞다.

중요한 것은 이 가죽이 사람의 것이냐 짐승의 것이냐가 아니다.

현재 옥좌에 앉아 있는 그자.

오랜 시간 정을 나누었던 수많은 벗과 뜻을 함게하던 동지들을 무참히 도륙하고, 그 서슬 퍼런 칼날을 자신들의 목까지 들이댔던 황제를 무너트리는 것만이 그들의 목표였다.

“그때처럼 힘없이 당할 수는 없소. 내 가문, 내 사람들을 살리기 위해서라도.”

“어찌하겠습니까. 한번 엎지른 물은 다시 주워 담을 수 없는 법. 황제…… 아니, 사 황자를 간과하던 우리 모두의 불찰이었습니다.”

“맞네. 하지만 그렇다고 한들 이미 더러워진 물을 굳이 주워 담을 필요는 없지.”

“백번 옳은 말씀이오. 물은 비워진 만큼 다시 채우면 되고, 금이 가고 피비린내 풍기는 그릇은 새로운 것으로 바꾸면 그만이지.”

한동안 그들은 신중한 목소리로 대화를 나누었다.

기호지세(騎虎之勢)라, 이미 성난 호랑이의 등에 올라탄 것과 다름없는 형국이니 남아 있는 선택지는 둘 중 하나뿐이었다.

지레 겁을 집어먹고 도중에 내려 호랑이에게 산 채로 씹어 먹히든가, 아니면 죽을힘을 다해 버티고 또 버텨서 제풀에 지친 호랑이의 뒷덜미에 비수를 꽂아 넣든가.

그리고 이 자리에 모인 이들은 모두 후자(後者)를 택했다.

좁게는 생존을 위해. 넓게는 위대하고도 찬란할 미래를 위해.

그렇게 저마다의 간절한 마음과 염원이 모여, 마침내 하나의 연판장(連判狀)이 탄생했다.

언젠가는 찾아올 역천(逆天)의 때를 기다리며.

다행히 그 기다림은 생각보다 길지 않았다.

황도가 피로 물들었던 그 날로부터 어언 십여 년.

가까스로 살아남은 노신(老臣)들의 머리 위에는 새하얀 서리가 내려앉았으나 그들이 절치부심하여 암암리에 키워 낸 세력은 더욱 단단하면서도 거대해졌고, 강보에 싸여 변방으로 떠났던 어린아이는 어엿한 소년이 되어 돌아왔으며, 황도에는 서서히 불온한 공기가 감돌고 있었다.

“이제는 모두가 황제를 주시하고 있소. 문무백관은 물론 무지몽매한 백성들까지.”

“소문을 퍼트림으로써 잠시 시간을 벌 요량이었는데, 부정하기는커녕 만천하에 공표하다니.”

“이번만큼은 그 교활하던 황제가 악수(惡手)를 뒀군. 공표까지 한 이상 불길은 걷잡을 수 없이 커질 테고.”

“사방에서 황제에 대한 추문(醜聞)이 끊이지 않고 있습니다. 그의 의도가 뭔지 짐작하기 어렵군요.”

“십 년이면 강산도 변한다지만, 사람은 쉽게 변하지 않지. 노부를 보게. 그때 당시에도 칠순이 넘었던 늙은이가 지금까지도 정정하게 버티고 있지 않나.”

“그 말씀은…….”

“황제도 마찬가지라는 걸세. 이건 놈이 파 놓은 계략이야. 어쩌면 다시 한번 피바람을 불러일으킬 속셈이겠지.”

정교한 인피면구로 중년인의 모습을 한 누군가의 늙수그레한 목소리에, 사람들은 낮게 침음성을 흘렸다.

조금도 예상하지 못해서?

아니다. 모두가 애써 외면하려는 현실을 날카롭게 꼬집은 한마디였기 때문이다.

그들도 정치라는 오물 판에서 한바탕 넘어지고 뒹굴며 살아남은 몸.

황제가 얼마나 잔혹하고 과감한 인물인지는 직접 보고 겪어서 익히 알고 있었다.

그럼에도 설마 그렇게까지 할까, 라는 의문을 쉽게 지울 수는 없었지만.

“과한 추측이 아닙니까? 정말 황제가 그럴 계획이라면, 그때는 정말 천하 각지에서 반란이 일어날지도 모릅니다. 아니, 분명 일어날 겁니다.”

누군가의 말에 중년인의 탈을 쓴 노신이 너털웃음을 터트렸다.

“당장 기거하는 저택의 세간살이며 곳간이 홀랑 다 타 버리게 생겼거늘, 저 멀리 천 리 밖에서 다가오는 불길이 대수겠는가?”

“……!”

“멍청한 소리는 집어치우고 부디 현실을 직시하게. 마 태감처럼.”

모두의 고개가 동시에 자신을 향해 쏠리자, 줄곧 오가는 이야기를 듣고 있던 마삼보가 오랜 침묵을 깨트리며 입을 열었다.

“역시 한림원(翰林院)의 동량지재들을 키워 내신 분다우십니다. 팔순이 넘으셨어도 총기는 여전하시군요.”

“마 태감. 그렇다면…….”

“저 역시 대학사(大學士) 어른의 말씀에 동감합니다.”

“……!”

“이는 단순한 개인으로서가 아닌, 동창 병필태감으로서 내린 판단이기도 합니다.”

사람들은 잠시 침묵했다. 마삼보가 병필태감이라는 직함까지 꺼내 들며 말했다는 것은 한 가지를 의미했기에.

“조정에…… 피바람이 불겠군.”

“그렇겠지요.”

누군가의 신음에도 마삼보는 흔들림 없는 목소리로 말을 이었다.

“하지만 그 바람에 섞인 피가 누구의 것일지는 이미 자명합니다. 폭풍은 이미 코앞까지 다가왔고, 서로가 가진 모든 힘을 꺼내어 부딪쳐야 할 겁니다.”

“마 태감. 외람되지만, 우리가 황제를 당해 낼 수 있겠소? 지금까지 알아낸 바에 의하면 저쪽의 전력이 예상했던 것보다 훨씬…… 흡.”

조심스럽게 말을 꺼낸 이는 곧장 후회했다.

그 순간 날아든, 칼날처럼 예리하고 서늘한 마삼보의 눈빛이 그의 가슴을 덜컥 내려앉게 만들었기 때문이었다.

“내가, 아니 제가 실언을 했습니다.”

나오지 않는 목소리를 쥐어 짜내어 건넨 사과에, 언제 그랬냐는 듯 눈빛을 거둬들인 마삼보가 담담히 대꾸했다.

“평소 같지 않게 경솔하셨소.”

“…….”

“서로를 믿고 한 배를 탔으니, 다 같이 함께 노를 저어야 앞으로 나아갈 수 있는 법. 그렇지 않소?”

“내 다시 한번 사과하리다. 진심으로 미안합니다.”

마삼보의 반응에 일순간 밀실 안의 공기가 냉랭해졌으나, 그 공기를 다시 훈훈하게 덥힌 사람 역시도 마삼보였다.

“걱정하지 마십시오. 우리에겐 황제를 끌어내릴 만큼 강한 명분과 힘이 있으니.”

“그 말씀은……?”

“모든 것을 말씀드릴 수는 없지만, 이번 대계(大計)를 위한 대비책은 충분히 세워 두었습니다. 이 이상 말씀드리지 못하는 부분에 대해 양해해 주시길.”

마삼보가 그렇게까지 말하자, 사람들은 입안에 감도는 의문을 고이 접어 마음 한구석에 집어넣었다.

비밀은 아는 사람이 적을수록 좋으니까.

더군다나 그들 역시 각자 크고 작은 힘과 영향력을 보탰지만, 마삼보는 이 계획에 있어 가장 중요한 핵심 인물 중 하나였다.

천하 인재의 요람이라 불리는 한림원의 대학사로서, 현직에서 물러난 지금까지도 조정을 주름잡고 있는 어느 노신처럼.

“한데, 그분께서는 어찌 지내고 계신가?”

불쑥 던진 물음에 담긴 뜻을 즉각 알아차린 마삼보가 대답했다.

“아직 무탈하십니다.”

“걱정이군. 황제가 틈만 나면 기회를 엿보고 있을 터인데.”

“그러나 뜻대로 되지 않겠지요. 감히 장담컨대, 현재로서는 황제도 쉽사리 그분께 마수(魔手)를 뻗치진 못할 겁니다.”

“황도 전체가 불 위에 놓인 솥단지처럼 끓어오르고 있네. 머지않아 사방으로 흘러넘치겠지.”

“대학사 어른께서는 그 시기를 언제쯤으로 보십니까?”

노신이 한 치의 망설임 없이 대답했다.

“연회. 황제가 이번 소문을 인정하며 공표했던 그 연회.”

“저 역시 그리 생각합니다.”

“홍문연(鴻門宴)이 되겠군. 서로의 창칼과 생사가 오가는.”

“홍문연과는 상황이 다를 겁니다. 초패왕 항우는 어리석었기에 유방을 살려 주었으나, 황제가 그럴 리 없을 테니까요.”

조용히 고개를 끄덕이며 생각에 잠겨 있던 노신이 문득 입을 열었다.

“그 젊은 강호인은? 어찌할 것 같나?”

“우리를 도울 겁니다. 예상했던 대로.”

“나이에 비해 고절한 무공의 소유자라는 이야기는 들었네. 허나 황제의 주위에는 그만한 고수들이 여럿 있어. 그자가 큰 도움이 되리라 보나?”

“글쎄요.”

마삼보가 희미하게 미소를 띤 채 말을 이었다.

“하지만 그 스승이 있다면, 이야기가 달라질 겁니다.”
```

## Final English reading copy

```markdown
# Chapter 881

They say rats hear what you say at night, and birds hear what you say by day.

But the guests who had gathered in a secret room early that morning at someone’s invitation weren’t the least bit troubled by such an old, tired saying.

Rats could be trampled to death. Birds could be shot down.

The only ones they had to worry about were the Embroidered Uniform Guard.

The Guard, little more than the Emperor’s watchdogs, wore golden armor the same yellow as a mongrel’s coat. Their specialty was combing every corner as if hunting for lice.

They sniffed out their target, tracked it down, sank their foul-smelling teeth into its neck, then ran back to their master, wagging their tails.

And with so many eyes and ears throughout the imperial capital, even the most secretive movements were bound to nag at them like a fish bone caught in the throat.

Perhaps that was why.

Though a dozen or so people had gathered in one place, an uncomfortable silence lingered in the secret room for some time.

Until the last person they were waiting for appeared with a faint noise.

Creeeak.

The old hatch overhead opened, and a dim shaft of light spilled in. Their eyes, accustomed to the darkness, narrowed reflexively, but they didn’t let down their guard.

They weren’t sure the unfamiliar man who had just stepped into the room was the ally they knew so well.

The newcomer immediately understood what their eyes were asking.

“Ah, my apologies. I was in such a hurry to get here that I forgot for a moment.”

Krrk. Crack.

“Hmm.”

A low groan rose from them all at once. The dozen or so guests watched the changes around the man with grave expressions.

Shhhk.

His features twisted like a wave.

His long philtrum shortened, his unusually prominent bulbous nose grew sharp, and an odd light appeared in his once-dull, unfocused eyes.

That alone was astonishing enough, but the changes didn’t stop there.

Crack.

With the sound of hundreds of bones shifting out of place, his body alternately shrank and stretched.

The transformation happened in an instant. In the time it took for a blink, not a trace of the man they’d just seen remained.

In his place stood a handsome man in his thirties or forties, with a lean build.

At last, the guests recognized the face before them and let go of the tension that had kept them taut.

“Your skill is as wondrous as ever.”

“We ought to be used to it by now, but we still tense up every time. Brush-Holding Eunuch Ma, your talent truly is remarkable.”

At the admiring remarks from all around, Ma Sanbao, the East Depot’s Brush-Holding Eunuch, smiled faintly.

“It’s just a parlor trick I happened to pick up.”

After modestly brushing off his astonishing disguise technique and Bone-Shrinking Technique, Ma Sanbao continued.

“More importantly, it seems everyone arrived at the appointed time. I hope the journey here wasn’t too inconvenient.”

The guests answered in more relaxed voices.

“It wasn’t as bad as I expected. Your loyal subordinates helped us, and we disguised ourselves much more thoroughly this time.”

“Of course, this ghastly thing is unpleasant and stifling, but what wouldn’t we endure to evade those Embroidered Uniform Guard bastards?”

Someone pointed to the human-skin mask stretched over his face. The others nodded in agreement.

That was right.

What mattered wasn’t whether this skin belonged to a person or an animal.

Their only goal was to overthrow the man sitting on the throne now—the Emperor who had brutally slaughtered countless friends with whom they had shared their affection for so long, and comrades with whom they had stood side by side in pursuit of their ideals, before turning that fearsome blade on them.

“We can’t let ourselves be crushed so easily again. Not if we want to save our families and our people.”

“What can we do? There’s no taking back water once it’s spilled. We were all at fault for underestimating the Emperor—or rather, the Fourth Prince.”

“Indeed. But that doesn’t mean we have to scoop up water that’s already dirty.”

“Couldn’t agree more. We can refill the vessel as it empties, and replace the cracked, bloodstained one with a new one.”

For a while, they spoke in measured voices.

They had ridden the tiger and were now clinging to its back. Only two choices remained: let fear drive them to climb down and be eaten alive, or hold on with all their might until the exhausted tiger could take no more—and plunge a dagger into the back of its neck.

Everyone gathered here had chosen the latter.

For survival, in the narrowest sense. And for a great and glorious future, in the broadest.

Thus, their fervent hopes and wishes came together, and at last a document bearing all their signatures was born.

They would wait for the day when the time came to defy heaven.

Fortunately, they didn’t have long to wait.

More than a decade had passed since the day the imperial capital ran red with blood.

White frost had settled on the heads of the old ministers who had barely survived, but the faction they’d secretly built with painstaking effort had grown even stronger and larger. The child who had left for the frontier, bundled in swaddling clothes, had returned as a boy. And an ominous air was slowly gathering over the imperial capital.

“Now everyone is watching the Emperor. The civil and military officials, and even the ignorant common folk.”

“We only meant to buy ourselves a little time by spreading the rumors, but instead of denying them, he announced them to the whole world.”

“For once, that cunning Emperor has made a blunder. Now that he’s made the announcement, the flames will grow beyond anyone’s control.”

“Scandalous stories about the Emperor keep surfacing everywhere. It’s hard to guess what he’s planning.”

“Ten years can change even mountains and rivers, but people don’t change easily. Just look at me. I was already past seventy back then, and I’m still going strong.”

“What do you mean…?”

“The Emperor is the same. This is one of his schemes. Perhaps he means to unleash another storm of blood.”

At the old-sounding voice of someone wearing a precise human-skin mask that made him look middle-aged, the others let out low groans.

Was it because they hadn’t expected it at all?

No. It was because his words had sharply pointed to the truth they were all trying to ignore.

They too had stumbled and rolled around in the filth of politics, and lived to tell the tale.

They knew firsthand just how ruthless and daring the Emperor was.

Still, it was hard to shake the question: would he really go that far?

“Isn’t that an overstatement? If the Emperor really intends to do that, rebellions might break out throughout the realm. No—they certainly will.”

At that, the old minister disguised as a middle-aged man burst into a hearty laugh.

“His own home, with all its furnishings and storehouses, is about to go up in flames. Why should he care about a fire approaching from a thousand *li* away?”

“……!”

“Stop saying foolish things and face reality. Like Brush-Holding Eunuch Ma.”

Every head turned toward him at once. Ma Sanbao, who had been listening quietly to the conversation, broke his long silence and spoke.

“It’s just as I’d expect from the man who nurtured so many pillars of the Hanlin Academy. Your mind is as sharp as ever, even past eighty.”

“Brush-Holding Eunuch Ma. Then…”

“I agree with His Excellency the Grand Secretary.”

“……!”

“This is not merely my personal judgment. It is my judgment as the East Depot’s Brush-Holding Eunuch.”

The others fell silent for a moment. Ma Sanbao had invoked his title as Brush-Holding Eunuch for a reason.

“Then a storm of blood will sweep through the court.”

“It will.”

Even as someone groaned, Ma Sanbao continued in an unwavering voice.

“But it’s already clear whose blood will be mixed into that wind. The storm is almost upon us, and both sides will have to throw everything they have into the clash.”

“Brush-Holding Eunuch Ma. Forgive me for asking, but can we really stand against the Emperor? From what we’ve learned so far, their forces are far beyond what we expected…”

The one who’d cautiously spoken regretted it at once.

Ma Sanbao’s eyes had shot toward him, cold and keen as a blade, making his heart sink.

“I—no, forgive me. I misspoke.”

He forced out his apology in a voice that would barely come. Ma Sanbao withdrew his gaze as if nothing had happened and replied calmly.

“That was unusually careless of you.”

“……”

“We’ve trusted one another and boarded the same boat. We have to row together if we’re going to get anywhere. Isn’t that right?”

“Let me apologize once more. I’m truly sorry.”

For a moment, Ma Sanbao’s response had chilled the air in the room. But he was also the one who warmed it again.

“Don’t worry. We have more than enough justification and strength to bring the Emperor down.”

“What do you mean…?”

“I can’t tell you everything, but we’ve made sufficient preparations for this great undertaking. Please understand that I can’t say more than that.”

When Ma Sanbao put it that way, the others quietly folded away the questions lingering on their tongues and tucked them into a corner of their hearts.

The fewer people who knew a secret, the better.

Besides, though each of them had contributed some measure of influence and power, Ma Sanbao was one of the key figures at the very heart of this plan.

Much like a certain old minister, once a Grand Secretary of the Hanlin Academy—the cradle of the realm’s talent—who still held sway over the court even after retiring from office.

“By the way, how is that person doing?”

Ma Sanbao immediately understood the meaning behind the sudden question and answered.

“That person is still safe.”

“I’m worried. The Emperor must be watching for an opportunity every chance he gets.”

“But he won’t get what he wants. I’ll say this with confidence: for now, even the Emperor won’t find it easy to reach that person with his evil designs.”

“The whole imperial capital is boiling like a pot left over a fire. Before long, it’ll spill over in every direction.”

“When do you think that will happen, Your Excellency?”

The old minister answered without the slightest hesitation.

“The banquet. The one the Emperor announced when he acknowledged the rumors.”

“I think so too.”

“It’ll be a Hongmen Banquet.[^1] Their spears and swords will decide who lives and dies.”

“It won’t be the same as Hongmen. Xiang Yu was foolish enough to let Liu Bang live, but the Emperor won’t make that mistake.”

The old minister quietly nodded, lost in thought. Then he suddenly spoke.

“What about that young martial artist? What do you think he’ll do?”

“He’ll help us. Just as we expected.”

“I’ve heard he possesses martial arts far beyond what you’d expect for his age. But there are several masters around the Emperor who are just as strong. Do you think he’ll be much help?”

“Who knows?”

Ma Sanbao continued with a faint smile.

“But if he has his master, that changes things.”

[^1]: At the historical Feast at Hong Gate, a banquet became the setting for an attempt on Liu Bang’s life.
```
