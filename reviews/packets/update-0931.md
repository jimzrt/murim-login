<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0931.txt",
      "sha256": "f8776a01263a60c4d816c836d4e86020a713e269cd4c3a0fdf6a0adfb4c7c326",
      "bytes": 12082
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f649c48fd6f9b24fcf058eede8727d325c92b0f1ee2d6ec098645ad7a27f5bb6",
      "bytes": 641
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "b6a95818bab6aabd835063ea8be17305ba85eb4844e119fd2921e1e3009f5ff3",
      "bytes": 778
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "239f09a74a7b46bc95ace272eaf3929dcc97c95e9e0210784a9c15d315c6124b",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "a2e59d21cb203b3c93294319d4be517db0edb91a7b08ffd4051c61097f44db10",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "f54b67da402cb130e55e7ae3f2538dbda2328e0c33006042ce9f8f88a0383e29",
      "bytes": 837
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3db98987b7cf2df7cd7f0eccd91ad8bef75b93e8d5dbe460aca6d9104f808c24",
      "bytes": 1445
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "7469d65f12c3c2b7dddab29f9bf9f39afb17f850f9066cb25482994db3894613",
      "bytes": 850
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 9701
}
-->

# Durable State Update — Chapter 931

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
1 and safe_through 931. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 931. Profile updates may replace only one
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
  "chapter": 931,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 931,
    "continuity_sources": [931],
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
    "Jin Taekyung has awakened after three days unconscious, with the Divine Physician, Jeok Cheongang, the Bow Saint, and his Fire Dragon Pavilion companions present."
  ],
  "continuity_sources": [
    930
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?"
  ],
  "safe_through": 930,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 공자      | **Young Master**                                                |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 930
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 928
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 927
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 930
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 927
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

## Korean source

```text
＃931화



사람이라면 누구나 혼자만의 시간이 필요하다.

이를테면 몇 년간 확인하지 않은 포털 사이트 메일함처럼 터질 듯이 쌓여 있는 시스템 메시지를 확인해야 할 때.

특히 십여 명이 보는 앞에서 자신의 중요 부위를 더듬고, 전율에 몸을 부르르 떤 뒤라면 더더욱 그렇다.

그러나 도무지 의미를 알 수 없는 악몽과 그 악몽보다도 더 끔찍한 상황을 겪은 후에도 사람들은 나를 홀로 내버려 두지 않기로 작정한 듯싶었다.

“자, 지금부터 저를 따라 팔을 들어 보십시오.”

“잘하셨습니다. 그럼 이번에는 조금 더 각도를 비틀어서…….”

“지금 제가 펼친 손가락이 몇 개인지 보이십니까?”

첫 번째로 맞이한 손님은 내가 의식을 되찾았다는 소식이 알려지기 무섭게 쳐들어온 어의(御醫)들이었다.

이미 사흘 전부터 황제의 엄명에 의해 대기하고 있었다는 그들은 탕약 냄새를 물씬 풍기며 내게 이런저런 일을 시키더니, 이내 심각한 얼굴로 서로 머리를 맞댄 채 소곤거렸다.

물론 그래 봤자 내 귀에는 선명하게 들렸지만.

“몸 상태는 정상, 아니 완벽하군.”

“엄청난 혈전이 벌어졌다고 들었는데, 희한할 정도로 멀쩡합니다. 상처 하나 없어요.”

“그뿐만이 아닐세. 좀 더 자세히 보면 수상할 정도로 앞섬이 부풀어 있어.”

“예? 그럼 저게 설마…… 그럴 리가요. 말도 안 됩니다.”

“사실 나도 확신하는 건 아니야. 적당한 틈을 봐서 신호를 줄 테니, 자네가 실수인 척 한번 눌러 보게.”

“음. 알겠습니다.”

짧은 의논을 끝마친 어의들은 온화한 미소를 지으며 돌아섰고, 혹시 모르니 다시 한번 몸을 살펴보겠다는 그들의 제안에 나는 망설임 없이 대답했다.

“당장 나가.”

하지만 어의들이 떠난 뒤에도, 내가 머무르는 전각을 찾는 발걸음은 끊이질 않았다.

“저기, 조장님. 손님이 찾아오셨는데요.”

“손님 누구.”

“잠시만요. 어, 그저께 새로 임명된 광록대부(光祿大夫)라고 하시는데.”

“광록대부가 정확히 뭐 하는 양반인데.”

“그거 알면 제가 무림인 안 했죠.”

“대충 듣기만 해도 사짜 냄새 풀풀 풍기네. 대출 안 받는다 그래.”

“예, 일단 그렇게 전할게요.”

광록대부라는 관직이 삼공(三公) 다음으로 높다는 사실을 알게 된 건, 수십여 명의 관리들을 돌려보낸 후에야 맞이한 새로운 손님 덕분이었다.

“이거 내가 한발 늦은 건 아닌가 모르겠네. 벌써부터 이렇게 문전성시(門前成市)를 이루는 걸 보면.”

친근함이 묻어 나오는 말투.

너스레를 떨며 들어오는 홍진의 모습에 내 입가에도 미소가 번졌다.

“홍 동지.”

“동지라, 혹시 말했던가요? 비록 관직명이긴 하지만, 진 공자가 나를 동지라고 불러 줄 때마다 항상 든든했었다고.”

장난기 가득한 표정. 그러나 홍진의 눈빛과 목소리에는 형용할 수 없는 마음이 가득 담겨 있었다.

“고마워요, 진심으로. 비록 오늘 이 자리에 함께 오지는 못했지만 황태제(皇太弟) 전하께서도 같은 마음이시라는 걸 알아줬으면 해요.”

스륵.

화려한 문양이 수 놓인 군청색 의복을 가다듬은 홍진은 정중하기 이를 데 없는 태도로 절을 올렸고, 고개를 들며 언제 그랬냐는 듯이 웃었다.

“아, 그리고 나 승진했어. 이제는 모두 홍 동지가 아니라 홍 태감(太監)이라고 불러.”

“태감이라면, 설마?”

“진 공자가 지금 생각하는 그곳이 맞아요. 실은 지난 세월 동안 아무것도 모르고 황제 폐하를 의심했던 게 죄송스럽고 부끄러워서 몇 번이나 사양하고 낙향하려 했었는데…….”

어느샌가 제법 눈에 익숙해진, 동창(東廠)의 복색을 한 홍진이 희미하게 웃으며 말을 이었다.

“폐하께서 그러시더라고. 앞으로 처리해야 할 일이 얼마나 많은데 혼자 내빼려 드냐고. 괘씸해서라도 못 놓아준다고.”

“잘됐네요. 진심으로.”

잘된 일이고, 동시에 옳게 된 일이다.

사실 지난 십여 년간 황제를 향해 있던 홍진의 적대감은 죄라고 할 것도 없었다.

그것은 황제가 의도적으로 진실을 감추었기에 벌어진 일이었고, 모든 것을 떠나 주표의 곁에 붙여 두었다는 것은 그만큼 홍진의 충성심을 믿었다는 반증(反證)이기도 했다.

“그럼 홍 동지, 아니 홍 태감이 동창의 새로운 창공(廠公)이 된 겁니까?”

“동창을 책임지고 있는 건 맞지만, 창공. 즉 장인태감이라는 지위는 영원히 공석일 가능성이 높아요. 역적의 흔적은 조금도 남겨 두지 않는 것이 대국의 방식이니까. 더군다나…….”

순간, 홍진의 눈동자가 서늘하게 빛났다.

“아직 뽑지 못한 잔뿌리가 남아 있으니까.”

그가 입에 담은 잔뿌리라는 단어가 어떤 것을 의미하는지, 나는 문득 알 것 같았다.

넓은 의미로는 동천마군의 그늘이 가장 짙게 드리워져 있던 동창 전체일 것이고, 좁은 의미로는 내가 의식을 잃기 직전까지 죽음이 확인되지 않았던 한 사람을 뜻하는 것일 터였다.

“마삼보.”

내 입술 사이로 흘러나온 그 이름에, 홍진이 작게 고개를 끄덕였다.

“지난 사흘 동안 황도는 물론 인근 수백 리를 샅샅이 뒤졌음에도 행적이 묘연해요. 마치 하늘로 솟은 것처럼.”

솔직히 이것만큼은 마삼보에게 내심 감탄할 수밖에 없었다.

그 긴박한 상황에서 몸을 빼내어 도주한 것으로도 모자라, 사흘 간 이어진 황군의 추격까지 피했다니.

‘이미 상당한 부상을 입은 상태였을 텐데. 어떻게 사라진 거지?’

물론 가능성은 충분했다.

비록 스승인 동천마군에게는 한참 못 미친다고는 해도 마삼보 역시 초절정의 경지에 오른 강자인 동시에 엄청난 회복력을 지닌 괴물이고, 특히 얼굴과 체격을 바꾸는 역용술(易用術)은 나조차도 혀를 내두를 정도였으니까.

‘마지막으로, 주위 어딘가에 숨겨 둔 암천의 이동진(移動眞)을 이용했을 가능성도 있지.’

마삼보는 반드시 죽여 후환을 없애야 할 대상이지만, 이미 손이 닿지 않는 곳까지 도망쳤다면 별다른 방법이 없다.

지금은 아직 그물을 빠져나가지 못한 사냥감들과, 저 멀리서 기척을 숨긴 채 다가오는 맹수들을 대비하는 것이 최선이다.

“홍 동…… 아니, 홍 태감.”

불쑥 입을 연 나를 향해, 홍진이 빙긋 웃었다.

“아무렇게나 편하게 불러요. 진 공자는 그래도 되는 사람이니까.”

“어이, 홍 씨.”

“……진짜 세상 편하게 부르네. 왜요?”

“부탁 하나만 해도 됩니까?”

“그걸 말이라고. 진 공자 부탁이라면 역모 빼고 다 할 테니까 뭐든 말해요.”

“그럼…….”

앞서 시원시원하게 대답한 홍진은, 이어진 내 말을 듣고 눈을 동그랗게 떴다.

“음?”

“안 됩니까?”

“아니, 당연히 어려운 부탁은 아닌데, 이게 도대체 무슨 의미를 담고 있는 건가 싶어서.”

“정말 중요한 일입니다. 보다 정확한 건 제가 직접 확인한 후에 알려 드릴 거고요.”

“당연히 그래야지. 아무것도 없이 맨입으로 넘어가면 쓰나. 동창 태감을 부려 먹는 일인데.”

너스레를 떨며 자리에서 일어난 홍진이 떠나자, 눈치를 살피고 있던 혁무진이 슬그머니 다가와 입을 열었다.

“저어, 조장님.”

“저게 도대체 무슨 부탁이냐고?”

“크, 역시 귀신이십니다.”

이 와중에도 엄지를 치켜세워서 아부를 떠는 혁무진의 모습에, 나는 피식 웃으며 고개를 저었다.

“있다. 그런 게.”

“어어, 저한테까지 비밀로 하시는 겁니까?”

“꼭 그렇다기보다는…….”

“그렇다기보다는?”

“나도 잘 몰라.”

“……?”

잠시 침묵하던 혁무진이 짜게 식은 눈빛으로 나를 응시했다.

“그냥 말해 주기 싫으면 싫다고 하십쇼. 사람 더 비참하게 만들지 마시고.”

“진짜야, 인마.”

“됐습니다. 당분간 저한테 말 걸지 마세요. 저도 말 안 할 테니까.”

삐친 티를 팍팍 내며 방을 나서려는 녀석의 뒷모습에, 나는 미안함을 담아 말을 건넸다.

“셋 셀 때까지 원위치. 하나.”

쉭.

둘을 세기도 전에 제자리로 돌아온 혁무진이 딴청을 피우며 물었다.

“그래서, 뭔데요?”

“말했잖아. 나도 정확히 뭔지 모른다니까.”

“……진짜요?”

“어. 그냥 누가 말해 준 거라서. 자세히도 아니고 대략적으로.”

“누가요?”

“있어. 너도 아는 사람.”

고개를 갸웃거리던 혁무진이 자신감 넘치는 표정으로 가슴을 탕탕 쳤다.

“누군지 말씀해 주시면 제가 당장 가서 데려오겠습니다. 이참에 조장님께서도 좀 더 자세히 설명을 들…….”

“그건 안 될걸.”

이어지려는 말을 끊어낸 내가 덧붙였다.

“그 사람, 이미 죽었거든.”

“예?”

“죽었다고. 그것도 내 손으로 직접.”

그때였다.

멍하니 입을 벌린 채 나를 바라보던 혁무진의 눈이 크게 뜨인 것은.

“서, 설마? 아니죠?”

“말해 줬으니까 가라. 나 좀 혼자 내버려 둬.”

“아니, 잠깐만요. 그 작자가 왜 조장님께……!”

“셋 셀 때까지 꺼져라. 물론 뒷일은 알아서 감당하고. 하나.”

쉭.

성능 한 번 확실하구만.

둘을 세기도 전에 사라진 혁무진의 빈자리를 보며 나는 헛웃음을 흘렸다.

그리고 부드러운 비단 침구에 몸을 파묻은 채, 밤이라는 사실이 무색하리만치 환한 창밖을 바라보았다.

‘환하네. 시끄럽고.’

내궁 깊숙한 곳에 위치한 전각임에도, 저 멀리 바람에 실려 들려오는 환호와 노랫가락을 들을 수 있었다.

드문드문 솟구친 폭죽은 화려하게 밤하늘을 수놓았고, 새로운 시대를 맞이한 백성들은 잠을 잊고 거리로 뛰쳐나와 밤새도록 웃고 떠들며 술잔을 기울일 터였다.

내일의 근심을 뒤로한 채, 그저 오늘의 기쁨을 마음껏 즐기며.

‘한때는 당신도 이런 세상을 바랐겠지.’

나는 더 이상 이승에 존재하지 않는 누군가를 떠올렸다.

마지막 순간 마음 안에 남아 있던 모든 분노를 내려놓고 인간으로서 죽음을 맞이한 그. 동천마군을.

그리고 유언이나 다름없었던 그의 전음(傳音)을.



‘지금부터 내가 하는 말을, 똑똑히 기억하게.’



이어진 그의 말은 짧고 간단했다.

어느 한 장소에서, 한 가지 물건을 찾으라는 것.

그것이 전부였다.

‘그리고 그 물건이 무엇인지는, 머지않아 곧 알게 되겠지.’

나도 모른다. 동천마군이 최후의 순간에 이르러 언급한 그 물건이 정확히 무엇인지. 어떤 내용과 의미를 담고 있는지.

다만 그 실체를 이 두 눈으로 직접 확인하기 전까지는 더 이상 생각하지 않기로 했다.

지금의 내게는 당장 처리해야 할 일들이 있었으니.

“시스템 창 오픈.”

나직한 목소리가 입술 사이로 흘러나온 그 순간.

띠링. 띠링. 띠리리리링!

미친 듯이 울려 퍼지는 종소리와 함께, 무수한 홀로그램 창이 시야를 뒤덮었다.

아주 오랫동안.

마치 이 순간만을 기다려 왔다는 듯이.
```

## Final English reading copy

```markdown
# Chapter 931

Everyone needs some time alone.

Say, when you need to check the System messages piled up until they’re ready to burst, like emails in a portal account you haven’t opened in years.

Especially if you’ve just groped your own private parts in front of a dozen people, then shuddered all over.

But even after I’d endured an incomprehensible nightmare—and a situation more horrifying than the nightmare itself—people seemed determined not to leave me alone.

“Now, please raise your arm and follow my movements.”

“Very good. This time, turn it at a slightly different angle…”

“Can you see how many fingers I’m holding up?”

My first visitors were the imperial physicians, who came charging in as soon as word spread that I’d regained consciousness.

They’d apparently been waiting on the Emperor’s strict orders since three days ago. Reeking of herbal decoctions, they had me do this and that, then huddled together with grave expressions and whispered to one another.

Of course, I could hear every word perfectly.

“His condition is normal—no, perfect.”

“I heard there was an enormous battle, but he’s bizarrely unharmed. Not a single wound.”

“That’s not all. If you look more closely, the front of his robe is suspiciously bulging.”

“What? You mean that could be…? No, that can’t be. It’s impossible.”

“To be honest, I’m not certain either. I’ll give you a signal when the opportunity arises. You can press it once, pretending it was an accident.”

“Hmm. Understood.”

The physicians finished their brief discussion, turned around with gentle smiles, and suggested they examine me one more time, just in case.

I answered without hesitation.

“Get out. Now.”

But even after the physicians left, there was no end to the people coming to the pavilion where I was staying.

“Um, Captain. Someone’s here to see you.”

“Who?”

“Just a moment. They say they were appointed Guanglu Dafu the day before yesterday.”

“What exactly does a Guanglu Dafu do?”

“If I knew that, I wouldn’t have become a martial artist.”

“Even just hearing the title, he sounds like a scammer. Tell him I’m not taking out a loan.”

“Yes, I’ll pass that along.”

I only learned that the Guanglu Dafu was an official whose rank came just below the Three Excellencies after turning away dozens of officials. Then, at last, I welcomed a new visitor.

“I hope I’m not too late. Looking at the crowds already gathered outside your door, you’re quite the popular man.”

His voice was warm and familiar.

Hong Jin came in with a joking air, and a smile spread across my face too.

“Comrade Hong.”

“Comrade? Have I ever told you? Even though it was an official title, whenever Young Master Jin called me Comrade, it always made me feel I could count on you.”

His expression was full of mischief. But Hong Jin’s eyes and voice held a feeling beyond words.

“Thank you. Truly. His Highness, the Emperor’s younger brother and heir, couldn’t come with me today, but I hope you know he feels the same way.”

*Swish.*

Hong Jin straightened his navy-blue robe, embroidered with ornate patterns, and bowed with the utmost respect. Then he raised his head and smiled as though nothing had happened.

“Oh, and I got promoted. From now on, don’t call me Comrade Hong. Call me Eunuch Hong.”

“Eunuch? Don’t tell me…”

“You’re thinking of exactly the right thing, Young Master Jin. I felt guilty and ashamed that I’d spent all those years suspecting His Majesty without knowing the truth. I turned down the position several times and even tried to retire to the countryside, but…”

Now wearing the uniform of the East Depot, a sight I’d grown fairly used to, Hong Jin continued with a faint smile.

“His Majesty said, ‘There’s so much left to take care of. How can you try to run off on your own? I’m not letting you go, if only because you’ve got the nerve to try.’”

“That’s good. Truly.”

It was good news—and the right outcome, too.

In truth, Hong Jin’s hostility toward the Emperor over the past decade or so wasn’t something he could be blamed for.

It had happened because the Emperor had deliberately hidden the truth. And, putting everything else aside, the fact that he’d kept Hong Jin by Zhu Bao’s side was proof of how much he trusted his loyalty.

“So, Comrade Hong—no, Eunuch Hong—have you become the East Depot’s new Cang Gong?”

“I’m responsible for the East Depot, yes. But the position of Cang Gong—the Seal-Holding Eunuch—may remain vacant forever. It’s the Great Nation’s way to leave no trace of a traitor behind. Besides…”

For a moment, Hong Jin’s eyes turned cold.

“There are still roots we haven’t pulled up.”

I thought I knew what he meant by “roots.”

In the broadest sense, it could mean the entire East Depot, where the Eastern Heaven Demon Lord’s shadow had fallen most heavily. More narrowly, it could mean one man whose death had not been confirmed by the time I lost consciousness.

“Ma Sanbao.”

At the name that slipped between my lips, Hong Jin gave a small nod.

“We searched the capital and hundreds of miles around it for the past three days, but there’s no trace of him. It’s as if he vanished into the sky.”

Honestly, I couldn’t help admiring Ma Sanbao, at least a little.

He’d managed to escape in the middle of that desperate situation—and then evade the Imperial Army’s pursuit for three straight days.

*He must have been badly wounded already. How did he disappear?*

Of course, it was entirely possible.

Even if he fell far short of his master, the Eastern Heaven Demon Lord, Ma Sanbao had still reached the Supreme Peak realm and was a monster with incredible powers of recovery. And his disguise technique, which could change his face and build, was good enough to make even me whistle in admiration.

*Lastly, he could’ve used a Moving Formation Dark Heaven had hidden somewhere nearby.*

Ma Sanbao was someone who had to be killed to eliminate future trouble. But if he’d already fled somewhere beyond our reach, there wasn’t much we could do.

For now, the best course was to prepare for the prey that hadn’t escaped the net yet—and the predators approaching from far away with their presence concealed.

“Comrade Hong… no, Eunuch Hong.”

Hong Jin smiled at me.

“Call me whatever you like. You’re allowed, Young Master Jin.”

“Hey, Hong.”

“…You really do make yourself at home. What is it?”

“Can I ask you a favor?”

“Why even ask? I’d do anything for you, Young Master Jin—anything but treason. So, name it.”

“Then…”

Hong Jin had answered so readily, but at my request he blinked in surprise.

“Hm?”

“Can’t you do it?”

“No, it’s not a difficult favor. I’m just wondering what it means.”

“It’s very important. I’ll tell you more precisely after I check it myself.”

“Of course you will. You can’t just expect me to do it for nothing. You’re making use of an East Depot eunuch, after all.”

Hong Jin joked as he stood and left. Hyuk Mujin, who’d been watching for an opening, sidled over and spoke.

“Um, Captain.”

“You’re wondering what that favor was?”

“Wow. You really are a mind reader.”

Even now, Hyuk Mujin raised his thumb and tried to butter me up. I chuckled and shook my head.

“There is something.”

“Wait, you’re keeping it secret from me too?”

“It’s not exactly that…”

“Not exactly?”

“I don’t know either.”

“……?”

Hyuk Mujin stared at me with a deeply unimpressed look.

“If you just don’t want to tell me, then say so. Don’t make me feel even more pathetic.”

“I’m serious, you idiot.”

“Forget it. Don’t talk to me for a while. I won’t talk to you either.”

As he headed for the door, making a big show of how offended he was, I called after him apologetically.

“Get back here before I count to three. One.”

*Whoosh.*

Hyuk Mujin returned to his spot before I could count to two, then asked while pretending to look elsewhere,

“So, what was it?”

“I told you. I don’t know exactly what it is either.”

“…For real?”

“Yeah. Someone just told me about it. Not in detail—just the gist.”

“Who?”

“Someone you know, too.”

Hyuk Mujin tilted his head, then thumped his chest with a confident look.

“Tell me who it is, and I’ll bring them here right away. Then you can hear all about it in greater detail…”

“That won’t work.”

I cut him off and added,

“That person’s already dead.”

“What?”

“They’re dead. And I killed them myself.”

That was when Hyuk Mujin, who’d been staring at me with his mouth hanging open, suddenly widened his eyes.

“Y-you don’t mean…? No, right?”

“I told you, so go. Leave me alone.”

“Wait, why would that bastard tell you…?”

“Get out before I count to three. And deal with whatever comes after on your own. One.”

*Whoosh.*

That sure works.

I let out a hollow laugh at the empty spot where Hyuk Mujin had been. He’d vanished before I could count to two.

Then I sank into the soft silk bedding and stared out the window, bright enough to make it hard to believe it was night.

*It’s bright. And loud.*

Even from this pavilion deep inside the Inner Palace, I could hear the distant cheers and songs carried on the wind.

Fireworks shot up here and there, painting the night sky in brilliant colors. The people, welcoming a new era, would have forgotten sleep and poured into the streets, laughing, talking, and drinking all night.

Leaving tomorrow’s worries behind to enjoy today’s happiness to the fullest.

*You wanted a world like this once, too.*

I thought of someone who no longer existed in this world.

The man who had laid down all the anger left in his heart at the very end and died as a human being. The Eastern Heaven Demon Lord.

And the Sound Transmission that had been all but his last words.

*“Remember every word I say from this moment on.”*

What he said next was short and simple.

Find one thing in one particular place.

That was all.

*And I’d find out what that thing was soon enough.*

I didn’t know either. I had no idea what that thing was, the one the Eastern Heaven Demon Lord had mentioned at the very end, or what it contained or meant.

But I decided not to think about it anymore until I could see it with my own eyes.

There were things I needed to deal with right now.

“Open System window.”

The instant the quiet words slipped from my lips—

*Ding. Ding. D-d-ding!*

A mad chorus of chimes rang out, and countless holographic windows filled my vision.

For a very long time.

As if they’d been waiting for this moment alone.
```
