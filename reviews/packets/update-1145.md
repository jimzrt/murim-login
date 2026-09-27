<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1145.txt",
      "sha256": "37f84d755e402a21223cbb16ebec0a6a229ffdc10a08ea1de21061450ccc0e96",
      "bytes": 12080
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1bbf5f648fecb5a9ce5577973b614d79f7475b507bff57beae4b9125167edf82",
      "bytes": 1601
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b92fbed718deaac7d0d56e7bd680d3b941bd535dbd0d843221acef0bede11f8d",
      "bytes": 245956
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6ec0e0237b77e1a97f2c91818a26134069e95989cfde90bcc06c3fd01f94602d",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "5723be2fc7c0c02fde8f1ce005d1b2eb2bc7142a4e3d72908a0a1bb50d1e077f",
      "bytes": 1583
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8c8f663f3697d95be541ece3934b6dc9f93d82ec00f7e626e8b9cfccc5b4c4cc",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "84b5dcb5ddcf9025fdaa79d72e5d940176cf9600e41145213438d723102d5edd",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "43439c3a04e26c1f05d2f90e119c4024c52f9919b19355186c9b78090a79fdc9",
      "bytes": 291243
    }
  ],
  "estimated_tokens": 9893
}
-->

# Durable State Update — Chapter 1145

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
1 and safe_through 1145. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1145. Profile updates may replace only one
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
  "chapter": 1145,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1145,
    "continuity_sources": [1145],
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
    "More than two hundred thousand Murim forces are marching from Xining toward a cursed forbidden land beyond the desert to fight the Lord of Heaven.",
    "Taekyung suspects The Helper was the Martial God and that the Martial God was Cheon Taemin; he theorizes the System preserved Cheon’s consciousness in the Inventory.",
    "The pocket watch’s hand has moved backward from the position Hyuk Mujin remembers, and its Item information says it holds a secret.",
    "Taekyung left Xining asleep in a prepared carriage to pursue an unspecified plan; Jeok Cheongang is waiting for him."
  ],
  "continuity_sources": [
    1143,
    1144
  ],
  "open_questions": [
    "Are Cheon Taemin and the Martial God the same person, and was Cheon’s consciousness preserved in the System?",
    "What is the pocket watch’s secret, and why did it return from the Inventory?",
    "What is the time ratio between the modern world and Murim?",
    "Who is The Helper, and what is his relationship to the System?",
    "What plan is Taekyung pursuing, and what will happen in the campaign against the Lord of Heaven?"
  ],
  "safe_through": 1144,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”",
    "Render 회중시계 as “pocket watch” and 누가 만들었는지 모를 회중시계 as “Pocket Watch of Unknown Make.”",
    "Render 팔황 as “Eight Directions” and 합종군 as “coalition army.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1142
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1144
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1144
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, and the Son of Heaven has formally enfeoffed him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1144
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1145화



화왕(火王) 적천강은 편안한 자세로 누워 있는 제자를 말없이 내려다보았다.

굳게 닫힌 눈꺼풀. 조용한 호흡과 함께 들썩이는 가슴.

지금의 진태경은 누가 보아도 세상 모를 만큼 깊은 잠에 빠진 모습이었지만, 적천강은 남들이 모르는 진실을 알고 있었다.

자신의 제자가 꿈속이 아닌, 또 다른 세상으로 떠났다는 것을.

‘선계(仙界).’

처음으로 제자의 입을 통해 진실을 마주했던 그 날의 충격을, 적천강은 똑똑히 기억하고 있었다.

아니, 잊을 수조차 없었다.

높이만 무려 수백 장에 달하는 마천루(摩天樓)가 한데 어우러져 숲을 이루고, 인간의 발자취가 하늘을 넘어 우주까지 닿았으며, 상리를 아득히 벗어난 괴력난신의 이치가 천하를 지배하는.

적천강으로서는 감히 상상도 할 수 없었던 미지의 세상.

그러나 제자가 나고 자랐다는 그 세상은, 처음 그가 생각했던 것만큼 평화롭고 아름다운 장소가 아니었던 것이 분명했다.



‘떠나야겠습니다.’



전날 밤, 고향으로 귀환하겠다는 뜻을 밝히던 진태경의 얼굴은 어느 때보다 굳어 있었다.

스승인 그조차도 본 적 없을 만큼.



‘선계에 무슨 변고라도 생긴 것이냐?’

‘모릅니다. 아직은.’

‘아직은, 이라. 네 녀석이 그리 말하는 것을 보아하니 필시 좋지 않은 일이 벌어지고 있는 모양이구나.’

‘어디까지나 제 짐작뿐이지만, 그렇습니다.’



진태경은 짐작이라는 두 글자로 일축했지만, 그를 누구보다 정확히 꿰뚫어 보고 있는 적천강은 이미 알고 있었다.

자신의 제자는 결코 허언(虛言)을 하지 않는다는 사실을.

가벼움을 넘어 때때로 경박해 보이기까지 하는 평소의 언행 뒤에는, 주위의 사소한 변화 하나에도 촉각을 곤두세우고 있는 맹수가 숨어있다는 것을.

그렇기에 더욱 선명하게 느낄 수 있었다.

진태경의 두 어깨를 짓누르고 있는 거대한 불안과 부담, 그리고 그런 제자의 모습을 마주한 순간 철렁 내려앉은 마음도.

아마도 그 때문이었을 것이다.

열흘 전, 자신의 품속에서 힘없이 늘어졌던 제자의 육신이 불현듯 떠오른 것은.



‘그럼 다시, 제대로 말해 보거라.’

‘예?’

‘조금 전 네 녀석의 입으로 떠난다 하지 않았느냐. 마치 영영 돌아오지 못할 것처럼.’



스승의 괜한 우려를 걱정해서일까.

비록 진태경으로부터 선계라 불리는 그곳의 모든 상황을 듣진 못했지만, 한 가지는 똑똑히 알고 있었다.

모든 것이 다른 두 개의 세상이라 할지라도, 혼(魂)이 소멸하면 육신도 죽는다.

어느 날 두 번 다시 깨어나지 못할 깊은 잠에 빠진 제자의 모습을 마주하는 것이, 스승은 무엇보다도 두려웠다.

그리고 영원과도 같았던 찰나의 침묵 끝에, 진태경은 웃으며 대답했다.



‘그럼…… 다녀오겠습니다. 반드시.’



하지만 어째서일까.

원했던 답을 들었음에도 적천강의 마음은 무겁게 가라앉아 있었다.

뜬눈으로 밤을 지새우고, 먼 길을 떠난 제자의 곁을 지키고 있는 지금까지도.

‘짧으면 앞으로 한 달.’

이십여 만의 대군이 저 광활한 신강의 타커라마간(塔克拉玛干) 사막을 횡단하기까지 걸리는 시간.

물론 어디까지나 예측에 불과하지만, 이미 모든 준비와 계산을 철저히 끝마친 관무 연합군은 파죽지세로 사막을 횡단하고 더 나아가 목적지에 닿을 것이다.

지난 천년 간 저주받은 땅으로 여겨졌던 바로 그곳, 천산(天山)에.

‘어떤 위험이 도사리고 있다 해도 상관없다. 노부가 널 지킬 테니.’

해야 할 일을 알고 있는 자는 두려움이 없는 법.

스승이 있어야 할 곳은 바로 제자의 옆이었고, 적천강은 진태경이 깨어나기 전까지 결코 이 자리를 떠나지 않을 터였다.

그 어떤 말 한마디 없었음에도 자연스럽게 찾아와 각자의 위치를 지키고 있는 이들 역시도.

“뭘 그리 쳐다보나?”

반쯤 눈을 감은 채, 마차 한구석에 앉아 있던 살성의 물음에 적천강이 대답했다.

“웬 불청객이 떡하니 앉아 있으니 뭐 하는 놈인가 하고 보고 있었지.”

“불청객? 내가 왜 불청객이지?”

“마차 주인이 초대하지 않았으니까.”

살성이 콧방귀를 뀌며 진태경을 향해 턱짓했다.

“착각이 과하군. 마차 주인은 자네가 아니라 저기 누워 있는 녀석일세. 이 마차도 자네가 아니라 황제와 제갈세가에서 선물한 거고.”

“하지만 난 스승이야.”

“그렇게 따지면 나도 스승이지. 귀한 가르침을 내린 적이 있으니까.”

“설마 그 유령 뭐시기 보법? 별로던데?”

“뭐? 별로? 느그 열화문은…….”

“느그? 이 대가리에 피도 안 마른 놈이 어딜 지금 어른한테…….”

황실 제일의 한혈보마(汗血寶馬) 여덟 마리가 이끄는 마차 안에서, 심지어 합계 나이만 이백 세가 넘는 두 노강호가 나누는 대화치고는 심히 당혹스러웠으나 적천강은 마음 한구석에 퍼져 가는 온기를 느끼고 있었다.

‘보고 있느냐, 너의 노력과 고통은 결코 헛된 것이 아니었다.’

본격적인 진군이 시작된 지 불과 한 시진도 되지 않았건만, 이 길고도 아득한 행렬에서 홀로 후미(後尾)를 차지한 팔두마차에는 참으로 많은 손님이 찾아왔다.

황제의 최측근을 호위하는 금의위와 구파일방을 비롯한 무림의 고수들까지.

그들 한 사람 한 사람이 이 거대한 군세 속에서도 손꼽히는 실력자들이었고, 당연하다는 듯이 합류를 청했다.

빚을 갚기 위해서.

마차의 주인이 지금껏 보여 준 그 위대한 헌신과 노력에, 조금이라도 경의(敬意)를 표하기 위해서.

만약 적천강이 으름장까지 놓아가며 돌려보내지 않았다면, 지금쯤 마차 주위는 최소 일천이 넘는 최정예 호위대에 둘러싸여 있을지도 몰랐다.

물론, 그러한 적천강의 위협에도 눈썹 하나 까딱하지 않고 버텨 낸 극소수의 이들도 있었다.

“어우, 또 저러시네.”

“기운들도 좋으시군.”

“쉿, 들리겠어요.”

문 틈새로 소곤소곤 흘러들어오는 익숙한 음성들에, 순간 울컥했던 적천강은 자신도 모르게 피식 실소를 흘렸다.

“갑자기 왜 웃나? 꼭 정신 나간 노인네처럼.”

“글쎄.”

떨떠름해진 살성의 시비에도 웃음이 쉬이 사라지지 않는 이유는, 아마도 기뻐서였을 것이다.

이 험난한 천하에서 제자를 제 몸만큼이나 아끼고 위해 주는 이가 자신만이 아니라는 것에서 오는, 소소하지만 커다란 기쁨.

비록 일찍이 세상을 등지고 사람을 멀리했던 그였지만, 하나뿐인 제자는 같은 길을 걷게 하고 싶지 않았다.

아니, 이 아이만큼은 달라야 한다.

의(義)를 좇고, 협(俠)을 행하며, 인(人)을 얻어야 한다.

지금도, 이후에도.

언제나. 영원히.

그리고 이와 같은 바람을 이루기 위해서, 스승은 무엇이든지 할 수 있었다.

설령 저 열사(熱沙)의 땅 너머에 지옥이 기다리고 있다 하더라도.

‘반드시.’

어느덧 깊게 가라앉은 두 눈동자가 창밖에 펼쳐진 드넓은 사막을 응시하던 그때.

쿠르르릉.

강렬하게 피어오르던 아지랑이 위로, 거대한 먹구름이 드리워지기 시작했다.



* * *



세상에서 벌어지는 모든 일은 동전의 양면과 같다.

빛이 있으면 어둠이 있고, 해가 지면 달이 떠오르는 것처럼.

누군가가 따스한 온기 속에서 눈을 감은 지 얼마 되지 않아, 수만 리 밖에 떨어진 어느 밀실(密室)에서 깨어난 누군가에게도 마찬가지였다.

아니, 깨어났다는 표현부터 잘못되었을지도 모른다.

지금 막 눈을 뜬 이는, 이미 두 번 다시 잠들 수 없는 몸이 되어 버렸으니까.

- 무슨 일이 있었던 것이냐.

마치 머릿속에서 울려 퍼지는 듯한 나직한 음성에, 한 차례 부르르 몸을 떤 수하가 대답했다.

“잠시 쓰러지셨습니다.”

- 쓰러졌다?

“예. 의식을 잃으신 듯했습니다만 속하가 감히 손을 댈 수 없어…….”

콰득.

말이 끝나기도 전, 보이지 않는 손에 의해 목이 졸린 수하의 얼굴이 창백하게 질렸다.

- 감히 거짓을 고하다니.

“커, 컥. 아닙. 아닙니다.”

대답 대신 스멀스멀 기어오른 무형의 기운이 전신을 속박하고 숨통을 조인다. 

가파른 숨을 토해 내며 필사적으로 항변하던 수하의 신형이 축 늘어지자, 그제야 밀실 전체를 짓누르던 기운도 씻은 듯이 사그라졌다.

망자가 된 그의 말이 모두 진실이었다는 깨달음과, 해결되지 않는 한 줄기 의문을 남긴 채.

‘의식을 잃다니, 도대체 어째서?’

짙은 어둠 속, 수하의 시체를 뒤로한 채 밀실을 빠져나온 그림자는 생각에 잠겼다.

찰나의 순간에 찾아온 알 수 없는 충격과 이어진 의식의 끊김.

그것은 실로 방대한 지식을 소유한 그림자로서도 도무지 설명할 수 없는 일이었다.

그리고 마치 부유하듯 수천 개가 넘는 계단을 오른 그림자의 신형은, 자신의 의문을 해결해 줄 유일한 존재의 앞에 이르러서야 멈추었다.

구구궁.

출입을 청하기도 전에 열린 거대한 철문.

빛이라고는 한 점 보이지 않는 완전무결한 어둠 속에, 바로 ‘그’가 있었다.

- 이 미천한 종복이, 위대하신 천주(天主)를 배알 하나이다.

경애 어린 음성으로 부르짖은 그림자는 곧장 엎드려 부복했다.

이미 인간의 한계를 아득히 벗어난 힘과 격을 갖춘 그림자였으나, 저 칠흑 같은 어둠에는 당장이라도 자신을 벌레처럼 짓뭉개 버릴 힘이 깃들어 있었다.

아니, 오히려 한 단계 성장했기에 더욱 그 전능함을 선명히 느낄 수 있었다.

- 네가 찾아오리라는 것을 알고 있었다.

그저 듣는 것만으로도 영혼을 얼어붙게 만드는, 저 고저(高低) 없는 음성에 희미하게 묻어나오는 환희도.



- 그 파동을 느꼈을 테니.

- ……!

- 무엇이 그리도 놀라운가. 대술사(大術士)여.



불현듯 일렁인 어둠이 그림자, 아니 대술사의 어깨를 부드럽게 감싸 안았다.

- 본래 뿌리와 가지는 한 몸이니, 나의 은총을 말미암아 새롭게 태어난 그대라면 느낄 수 있었으리라.

일순간, 파르르 떨리는 대술사의 눈동자가 자신의 손에 닿았다.

이미 죽어 버린 육신을 일깨워 주듯 온통 썩고 문드러져 새하얀 뼈가 드러난 그 모습은 보는 이로 하여금 섬뜩함을 자아내기에 충분했지만, 대술사는 기쁨과 전율에 몸서리쳤다.

맞다.

자신은 다시 태어났다.

위대하고 전능한 천주의 축복 아래, 죽음을 딛고 일어나 다시 주인의 곁으로 돌아왔다.

그리고 마침내 깨달았다.

천주가 그린 대계(大計)의 진정한 목적을.



- 하면, 천주께서 말씀하신 조금 전의 파동은…….

- 그래.



바로 그 순간. 

스아아.

칠흑 같던 어둠 속에서 흐릿한 녹광(綠光)이 피어올랐다.

지난 오십여 년의 세월 동안, 지금껏 암천의 그 누구도 대면하지 못했던 새하얀 손가락이 녹광에 물든 옥을 어루어만졌다.

부드럽고, 서늘하게.

- 또 한 번, 하늘이 열렸구나.
```

## Final English reading copy

```markdown
# Chapter 1145

The Fire King, Jeok Cheongang, silently looked down at his Disciple, who lay in a comfortable position.

His eyelids were firmly shut. His chest rose and fell with each quiet breath.

Anyone could see that Jin Taekyung was in a deep sleep, oblivious to the world. But Jeok Cheongang knew the truth no one else did.

His Disciple had gone somewhere beyond his dreams—to another world.

*The realm of immortals.*

Jeok Cheongang remembered clearly the shock he’d felt that day, when he first heard the truth from his Disciple’s own lips.

No—he could never forget it.

A world where skyscrapers hundreds of *jang* tall stood together like a forest; where the footsteps of humanity reached beyond the sky and into the universe; where supernatural powers that defied all reason ruled the land.

An unknown world Jeok Cheongang could scarcely imagine.

But the place where his Disciple had been born and raised was clearly not as peaceful and beautiful as he’d first thought.

“I have to go.”

The previous night, Jin Taekyung’s face had been more solemn than ever as he said he intended to return to his homeland.

Even Jeok Cheongang had never seen him like that.

“Has something happened in the realm of immortals?”

“I don’t know. Not yet.”

“Not yet, you say. From the way you put it, something bad must be happening.”

“It’s only a hunch, but yes.”

Jin Taekyung had dismissed it with the words *only a hunch*, but Jeok Cheongang, who understood him better than anyone, already knew.

His Disciple never spoke idly.

Behind his usual lighthearted manner, which sometimes bordered on frivolous, lurked a beast alert to even the smallest changes around him.

That was why Jeok Cheongang could feel it all the more clearly.

The immense anxiety and burden pressing down on Jin Taekyung’s shoulders—and the way Jeok Cheongang’s heart had sunk when he saw his Disciple like that.

Perhaps that was why the image of his Disciple’s limp body, hanging helplessly in his arms ten days ago, had suddenly come to mind.

“Then say it properly this time.”

“What?”

“You just said you were leaving. As if you might never return.”

Maybe he’d been worried about his Master’s needless concern.

Jeok Cheongang hadn’t heard everything about the place called the realm of immortals, but he knew one thing for certain.

Even if the two worlds were different in every way, when the soul was erased, the body died too.

More than anything, a Master feared the day he might find his Disciple in a deep sleep from which he would never awaken.

And after a moment of silence that seemed to last forever, Jin Taekyung smiled and answered.

“Then… I’ll be back. I promise.”

And yet, why was it?

Even after hearing the answer he’d wanted, Jeok Cheongang’s heart had sunk heavily.

He’d stayed awake all night, and even now, as he remained beside his Disciple on the long journey, his heart was still weighed down.

*As little as a month.*

That was how long it would take an army of more than two hundred thousand to cross the vast Taklamakan Desert in Xinjiang.

It was only an estimate, of course. But the coalition army, having completed every preparation and calculation with meticulous care, would cross the desert at breakneck speed and reach its destination.

That very place which had been regarded as cursed for the past thousand years: Tianshan.

*No matter what danger lies ahead, it makes no difference. This old man will protect you.*

Those who know what they must do have no fear.

A Master belonged beside his Disciple, and Jeok Cheongang would not leave this spot until Jin Taekyung woke.

Nor would the others, who had arrived and taken up their positions without a word.

“What are you staring at?”

Jeok Cheongang answered the Slaughter Saint, who sat in one corner of the carriage with his eyes half-closed.

“There’s an uninvited guest planted right there. I was wondering who the hell he was.”

“Uninvited? Why would I be uninvited?”

“Because the owner of the carriage didn’t invite you.”

The Slaughter Saint snorted and nodded toward Jin Taekyung.

“You’re mistaken. The owner of the carriage isn’t you. It’s that fellow lying over there. And this carriage was a gift from the Emperor and the Zhuge Clan, not you.”

“But I’m his Master.”

“By that logic, I’m his Master too. I gave him some valuable instruction once.”

“You mean that Ghost-whatever footwork technique? It wasn’t very good.”

“What? Not very good? Your Fire Gate Clan—”

“Your? You snot-nosed brat. How dare you talk to an elder like that—”

It was a bewildering conversation for two old masters, whose combined ages exceeded two hundred, to be having inside a carriage drawn by the eight finest imperial sweat-blood horses. And yet Jeok Cheongang felt warmth spreading in one corner of his heart.

*Do you see? Your efforts and pain weren’t in vain.*

Not even one shichen had passed since the army began its full-scale march, yet the eight-horse carriage at the very back of the long, seemingly endless column had already received plenty of visitors.

The Embroidered Uniform Guard protecting the Emperor’s closest confidants, masters from the Nine Sects and One Gang, and others from Murim.

Every one of them was among the most skilled in this vast army, and each had come asking to join them.

To repay a debt.

To show even a little respect for the great devotion and effort the owner of the carriage had shown until now.

If Jeok Cheongang hadn’t sent them away with threats, there might have been more than a thousand of the finest guards surrounding the carriage by now.

Of course, a handful had stood their ground without so much as a twitch of the eyebrow, even in the face of Jeok Cheongang’s threats.

“Good grief, there they go again.”

“They’ve got plenty of energy.”

“Shh. They’ll hear you.”

At the familiar voices drifting in through the carriage door, Jeok Cheongang felt a sudden swell of emotion, then let out a small laugh before he knew it.

“Why are you laughing all of a sudden? You sound like a crazy old man.”

“Who knows.”

Perhaps Jeok Cheongang couldn’t stop smiling even after the Slaughter Saint’s sour jab because he was happy.

It was a small but profound joy, knowing that he wasn’t the only one in this harsh world who treasured his Disciple as much as himself and looked out for him.

Though Jeok Cheongang had turned his back on the world long ago and kept his distance from people, he didn’t want his one and only Disciple to walk the same path.

No. This boy had to be different.

He had to pursue righteousness, practice chivalry, and win people’s hearts.

Now, and from here on.

Always. Forever.

And to make that wish come true, his Master could do anything.

Even if hell waited beyond those scorching sands.

*I swear it.*

By now, Jeok Cheongang’s eyes had sunk deep as he watched the vast desert outside the window.

Then—

Rumble.

A huge bank of dark clouds began to spread above the intense heat shimmer.

* * *

Everything that happens in the world has two sides, like a coin.

As there is darkness where there is light, and the moon rises when the sun sets.

Not long after someone closed their eyes in comforting warmth, the same was true of someone who awoke in a sealed chamber tens of thousands of *ri* away.

No—perhaps *awoke* was the wrong word.

The one who had just opened their eyes had become someone who could never sleep again.

“What happened?”

At the low voice that seemed to ring inside his head, a subordinate shuddered and answered.

“You collapsed for a moment.”

“I collapsed?”

“Yes. It seemed you lost consciousness, but this subordinate dared not touch you…”

Crack.

Before he could finish, an invisible hand squeezed his throat, and the subordinate’s face went pale.

“You dare lie to me.”

“C-cough. I-I’m not.”

Instead of an answer, formless energy crawled over him, binding his whole body and constricting his breath.

The subordinate gasped and struggled to plead his case. When his body finally went limp, the energy pressing down on the entire chamber faded as though it had been washed away.

Leaving behind the realization that the dead man had told the truth—and one question that remained unanswered.

*Lost consciousness? Why?*

The shadow left the sealed chamber, its subordinate’s corpse behind it, and fell into thought amid the deep darkness.

An inexplicable shock had struck in an instant, followed by a break in consciousness.

Even the shadow, with its vast knowledge, could not explain what had happened.

The shadow rose as if floating, climbing thousands of steps. It stopped only when it reached the one being who could answer its question.

Rumble.

The enormous iron doors opened before the shadow could even ask to enter.

In the perfectly complete darkness, where not a single glimmer of light could be seen, *he* was there.

“Your humble servant comes before the great Lord of Heaven.”

The shadow cried out in reverence and immediately prostrated itself.

The shadow already possessed power and stature far beyond the limits of a human being. Yet that pitch-black darkness held a power that could crush the shadow like a bug at any moment.

No—in having grown another level, the shadow could feel that omnipotence all the more clearly.

“I knew you would come.”

Even the sound of that voice, so devoid of highs or lows that it froze the soul just to hear it, carried the faintest hint of delight.

“You must have felt the wave.”

“……!”

“What surprises you so, Grand Mage?”

A shadow stirred, then gently wrapped around the Grand Mage’s shoulder.

“Root and branch are parts of the same whole. Reborn through my grace, you must have felt it.”

The Grand Mage’s eyes trembled. For a moment, they turned toward their own hand.

It was rotted and decayed, white bone showing through—a chilling reminder that the body had already died. But the Grand Mage shuddered with joy and awe.

That was right.

They had been born again.

Under the blessing of the great and omnipotent Lord of Heaven, they had risen from death and returned to their master’s side.

And at last, they understood.

The true purpose behind the Lord of Heaven’s grand design.

“Then, the wave you spoke of just now…”

“Yes.”

At that very moment—

Ssssh.

A faint green light rose in the pitch-black darkness.

For more than fifty years, no one in Dark Heaven had seen the Lord of Heaven’s snow-white fingers. Now those fingers, bathed in green light, gently caressed a piece of jade.

Softly, and coolly.

“Once again, the heavens have opened.”
```
