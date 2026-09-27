<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1108.txt",
      "sha256": "c501d262f1b001c113a858b092add74ddcc10c0fc49bf9e42a03e54b4fb22788",
      "bytes": 13358
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f5a71dc8ac182e735a0e537aa3034c138f2535ca335264f3243d3a97bffd4162",
      "bytes": 1187
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2195176fcecc1f2d4760ffbc4a2601370e7609089bc148ea8deda43236c266fc",
      "bytes": 244248
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "6c584380189a3ec3c277169e5506b652cdb74387f524cd2cd1734f1281b7672b",
      "bytes": 941
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "38492b3693f317751824549f84dd6bbc7c72466e2c81ed390a9b829d4162c589",
      "bytes": 1120
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f10523d8e4b6126709d8cb4afc6edea0cdebd4b19e474b69aa6b9eb899c03348",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1891b6c92db00cfc69e5a0a3be3d80c0a5333a49207bfe1601d35fd1d5b8b478",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a524ce01f0d6a3e9aae37d3ccfebbe2c41f0a912450a7f5802e1cbfca55d2423",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3587b35f9f46255635c2b9217320b6613dd49879b3cf950be82def2526ffc095",
      "bytes": 288328
    }
  ],
  "estimated_tokens": 10504
}
-->

# Durable State Update — Chapter 1108

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
1 and safe_through 1108. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1108. Profile updates may replace only one
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
  "chapter": 1108,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1108,
    "continuity_sources": [1108],
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
    "Dark Heaven and the Potala Palace are attacking Xining; fighting continues at the breached western wall.",
    "Taekyung’s One Annihilation engulfs the Blood Lord, but the result is unknown.",
    "An unidentified attacker using the Zaha Divine Technique cuts the Black Ghost that the Blood Lord placed between himself and Taekyung.",
    "Jeok Cheongang remained at the North Gate to face the Potala Palace forces as of chapter 1105."
  ],
  "continuity_sources": [
    1106,
    1107
  ],
  "open_questions": [
    "Does Taekyung survive using One Annihilation, and does the Blood Lord survive its flames?",
    "Who intervened with the Zaha Divine Technique?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who are the allies approaching by river from the east?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1107,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 살기     | **killing intent**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 화산     | **Huashan**            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1107
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but suspects the Lord wants Jin Taekyung above all else; despite that, he attacks Taekyung, whom he considers a formidable adversary, as well as Cheongpung.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1103
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1107
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1107
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1107
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1108화



자신은 죽었다.

아니, 죽었다고 생각했다.

지금으로부터 일각 전, 무아지경에 휩싸여 위험을 감지하지 못한 진태경의 앞을 황급히 가로막았던 청년은 분명 죽음을 직감했었다.

하지만 아니었다.

미증유의 기운이 실린 핏빛 섬광에 이어 전신을 후려치는 거대한 충격.

그리고 마침내 잠시 끊어졌던 의식의 끈을 부여잡고 눈을 떴을 때, 돌무더기 속에 파묻혀 있던 청년은. 아니, 청풍(淸風)은 마음속으로 뇌까렸다.

‘태어나서 이렇게 위험했던 건 처음……이 아니네.’

만약 과거였다면, 정확히는 숭산(崇山)에서의 그 일을 겪지 않았다면 두려움에 떨었을지도 몰랐다.

태어나서 처음 겪어 보는 죽음에 대한 공포에, 맑은 냇물과 매화 향이 가득하던 연화봉(蓮華峰)에서는 느낄 수 없었던 살기와 광기에 압도당한 채 얼어붙었을 것이다.

그러나.

‘움직여야 해.’

이제는 달랐다.

화산에서 아름다운 자연을 거닐던 아이는 강호에 나와 뛰는 법을 배웠다.

세상의 추악한 일면을 마주하며 분노라는 감정을 알았고, 좋은 사람들과 함께하며 인의(人義)가 어떤 것인지 깨달았다.

그렇기에, 숱한 위협과 고난이 기다리고 있다는 사실을 알고 있음에도 다시금 일어날 수 있었다.

그것이야말로 자신을 키워 준 조부가 알려 준 정도(正道)요, 진태경을 보며 배운 협(俠)이었으므로.

‘가자. 은인에게로, 저들에게로.’

청풍은 비틀거리는 몸을 일으켜 세웠다.

전신을 짓누르고 있던 돌무더기를 밀어 내고, 군데군데 부러진 뼈마디에서 느껴지는 통증을 참아 내며 천천히.

그리고, 그 어느 때보다 은밀하게.



‘무공을 가르쳐 달라고?’



어느새 몸 곳곳에 아로새겨진 크고 작은 상처에서 흘러나오는 출혈 때문일까, 흔들리는 시야 속에서 언젠가 살성(殺星)과 나누었던 대화가 귓전에 울려 퍼지는 듯했다.



‘그게 무슨 뜻인지는 알고 하는 말이냐?’

‘어어, 아마도요.’

‘기가 막히는군. 다른 누구도 아닌 검성의 제자가, 한낱 살수(殺手)가 되려 한다니.’

‘네?’

‘멍청한 놈. 애초에 나는 무공이 아니라 살법(殺法)을 익힌 사람이다. 네 녀석과는 맞지 않아.’



그때의 살성은 쓴웃음과 함께 고개를 절레절레 내저었었다.

다음 순간, 청풍의 대답을 듣기 전까지는.



‘어라, 전 그렇게 생각하지 않는데요.’

‘뭐?’

‘할아버지께서 그러셨어요. 중요한 것은 도구가 아니라 도구를 쥔 사람이라고. 그런 의미에서 오래전에 봤던 어느 살수는, 결코 아무 이유 없이 누군가를 해칠 만한 사람이 아니었다고.’

‘……!’

‘맞다, 또 그런 말씀도 하셨어요. 앞으로 이 세상에서 스쳐 지나가는 이들은 모두 제 스승이자 은인이 될 수 있다고요.’

‘……너.’

‘잘 부탁드립니다. 작은 할아버지!’



말없이 자신을 바라보다, 이내 복잡해진 표정으로 입을 열었던 살성의 모습을 떠올리며 청풍은 낮고 조용히 숨결을 내뱉었다.

후우.

출혈과 고통으로 두방망이질 치던 심장이 잔잔해진다. 몸 곳곳에서 흘러나오던 피가 서서히 멎고, 인기척을 지운다.



‘한 가지만 익히기에도 녹록지 않을 것이다. 시간도, 상황도 따라주지 않을 테니.’

‘와, 지금 허락하신 거 맞죠? 그렇죠?’

‘빌어먹을. 그래. 하지만 한 가지 조건이 있다.’

‘조건이요?’

‘앞으로 두 번 다시, 나를 그따위 호칭으로 부르지 말아라.’

‘네. 작은 스승님!’

‘이런 제기랄.’

‘앗. 죄송해요. 작은 할아버지.’

‘……검성은 도대체 너 같은 미친놈을 어디서 주워 온 거냐?’



아마도 그때의 살성은 몰랐을 것이다.

청풍과 함께 시작한 여정이 채 한 달을 넘기기도 전, 그날 느꼈던 의문을 전혀 다른 의미로 내뱉게 될 줄은.



‘……검성은 도대체 이런 미친놈을 어디서 주워 온 거지?’

‘할아버지 말씀으로는 황새가 물어다 줬대요. 은인은 그런 게 아니라 배란 수정 착상이라고 했는데, 저는 무슨 소리인지 도무지 이해할 수가 없더라고요.’

‘……정말이지, 이해할 수가 없군.’

‘그렇죠? 저런 해괴한 말은 태어나서 처음 들어봐요.’

‘……나 역시 처음이다. 이런 해괴한 경우는.’



황당함에 물들어 있던 살성의 얼굴이 눈앞에 떠오른다.

그와 동시에, 어느샌가 깃털처럼 가벼워진 청풍의 발끝도 함께 피 웅덩이를 밟았다.

아니, 스쳤다.

스륵.

유령환살보(幽靈幻殺步).

고금제일의 살수가 창안한 독문 무공이자, 그 은밀함으로는 천하의 어떤 무공도 따라올 수 없다는 보법이 청풍의 발끝을 따라 펼쳐지고 있었다.



‘작은 할아버지 말씀이 맞았어요. 역시 쉽지 않네요.’

‘……그게 고작 한 달 만에 삼성(三成)에 다다른 놈이 할 소리냐?’



다른 누구도 아닌, 고금제일의 살수라 불리는 살성의 독문 무공.

하지만 청풍은 바로 그 유령환살보를 눈부신 속도로 터득했다.

누군가에게 있어 ‘고작’ 한 달밖에 안 되는 시간은, 그에게 있어 ‘무려’ 한 달이나 되는 시간이었으니까.



‘저, 무공 좋아해요. 그것도 아주아주.’

‘그건 나도……. 미치겠군. 도대체 어떻게 이게 가능하지?’



가능했다.

청풍에게는 그 모든 것이 숨을 쉬는 것과 같았으니까.

눈으로 보고, 몸으로 움직이면 어느 순간 자연스럽게 자신의 것이 되었다.

말에 담긴 뜻 그대로, 청풍 본인의 색이 섞여 재탄생한 그만의 새로운 무공으로.

쉭.

청풍의 신형이 나아간다.

빠르지도 느리지도 않은 속도로 뻗어가는 발걸음을 따라, 오직 그만이 맡을 수 있는 매화 향이 퍼져 나오는 듯했다.

암향표(暗香飄).

쏟아지는 빗줄기 사이로 번져 가는 화산의 매화 향은, 살성과 함께 한 지난 반년의 시간 속에서 구성(九成)에 다다른 유령환살보와 만나 더욱 조용하고 은밀해져 있었다.

두 눈으로 보아도 그 실체를 정확히 알아차릴 수 없을 만큼.

쉬쉬쉬쉭!

“크아악!”

푹, 서걱!

“천상천하, 만마……. 커헉!”

더는 걷잡을 수 없는 난전(亂戰)이 사방에서 벌어지고 있었음에도, 그 누구도 자신들을 스쳐 지나가는 청풍의 존재를 제대로 인지하지 못했다.

전장의 중심부를 가로지르는 청풍은 어느덧 주위의 모든 것에 자연스럽게 녹아들어 있었다.

모두의 머리 위로 쉼 없이 떨어져 내리는 빗줄기였고, 잠력단의 약효와 광기에 취한 암천의 광신도인 동시에 그들을 막는 무림인이며 관군이기도 했다.

그는, 이 혼란스러운 전장의 일부이자 그 자체였다.

오직 한 방향을, 한 사람만을 향해 나아가는.

‘은인.’

청풍은 보았다.

고오오옹.

일순간 보이지 않는 손이 움켜쥔 것처럼 일그러지는 공간 속, 끔찍하리만치 거대한 힘을 일거에 쏟아 내려는 진태경의 모습을.

더불어 그런 그를 향해 쏘아지는 혈주의 모습과, 오직 이 순간만을 기다렸다는 듯이 사각에서 짓쳐 들고 있는 칠흑빛 신형을.

‘늦었어.’

본능이 속삭인다.

안타깝지만 이것으로는 부족했다고.

지금의 청풍에게는 혈주를 쓰러트릴 만한 힘도, 시간도 주어지지 않았다고.

하지만.

‘할 수 있어. 은인이라면.’

그건 추측이 아니었다. 확신이었다.

추호의 흔들림조차 없는, 진태경을 향한 믿음.

그랬기에, 청풍은 망설임 없이 쏘아질 수 있었다.

화아아악.

아득한 섬광을 뿜어내며 터져 나온 그 거대한 화염을 향해서.

그 미증유의 힘을 상쇄하고자, 스스로의 몸뚱어리를 방패막이로 내던진 흑귀를 향해서.

팟.

시간이 느려진다. 공간이 지워진다.

일섬의 발출 직전, 굳게 자물쇠를 걸어 잠근 눈꺼풀 사이로 스며든 섬광이 바늘처럼 망막을 찌른다.

그러나 청풍은 선명하게 느낄 수 있었다.

자신이 나아가는 방향 끝에 서 있는 흑귀의 존재를.

저 안타까운 존재를 향해 한 줄기의 선을 그리고 있는 지금의 이 일격을.

그리고.

서걱.

무음(無音)에 가까운 절삭음과 함께 흑귀를 스쳐 지나간 순간, 벼락과도 같은 전율이 등줄기를 타고 솟구쳤다.

곧이어 조금 전 그가 지나쳐 간 공간을 집어삼키는, 끔찍한 열기로도 지워지지 않을 전율이.

‘해냈다.’

그와 동시에, 한 마리의 거대한 화룡이 힘없이 기울어지는 흑귀의 몸뚱어리를 집어삼켰다.

아니, 정확히는 그 너머에서 달려들던 핏빛 괴물을.

콰아아아아아!

막강한 충격파에 휩쓸려 날아가는 와중에도, 청풍은 소리 내어 웃었다.

마침내 터져 나온 불의 기둥에 의해 산산이 부서지고 있는 적도(赤刀)를 바라보며.

하지만 그는 몰랐다.

지금 이 순간, 사방을 물들이는 검푸른 화염을 바라보고 있던 한 사람.

진태경의 얼굴은 그 어느 때보다 차갑게 굳어 있다는 사실을.

쿨럭.

창백하게 질린 피부와 흐릿해져 가는 눈동자.

그러나 한 됫박이나 되는 핏물을 쏟아 내면서도, 진태경은 자꾸만 감겨 오는 눈꺼풀을 들어 올려 자신이 불러일으킨 불의 파도를 바라보았다.

이 세상에서 오직 그만이 들을 수 있는 가장 확실한 정보를 받아들이며.



- 삐빅! 삐비비빅!



온 힘을 기울였다.

모든 것이 텅 비어 버린 육신과 메마른 감각으로 상황을 인지했다.

하지만 보이지도, 들리지도 않는다.

허공에 떠오른 무수한 홀로그램 창도. 쉼 없이 귓가를 울리는 시스템 경고음 속 어디에서도.

적의 죽음을 알리는 맑은 종소리는, 끝끝내 들려오지 않았다.

창대를 버팀목 삼아 버티고 있던 두 다리가 힘없이 꺾이는 그 순간까지도.

철퍽.

그리고 진태경의 무릎이 피 웅덩이에 처박힌 그 순간.

투둑. 투두둑.

반경 수십여 장을 휘감은 불의 파도 속에서, 까맣게 타들어 간 괴물의 육신이 일어섰다.



* * *



갈증.

그것이 의식을 되찾은 혈주가 가장 먼저 느낀 감정이었다.

‘도대체 무슨 일이 있었던 거지?’

모른다. 알 수 없다.

아무것도 기억나지 않았다.

자신이 누구인지. 어떤 인생을 살아왔는지조차 떠오르지 않았다.

그저 이 끔찍한 갈증을 해소하기 위한 본능만이 남아 몸을 지배할 뿐.

사박.

비틀거리며 내디딘 발걸음 소리는 사막을 걷듯이 건조했다.

어째서일까.

혈주는 마음속으로 멍하니 뇌까렸다.

분명, 이곳 어딘가쯤에 이 갈증을 채워 줄 무언가가 있을 줄 알았는데.

그런 줄 알았는데.

‘도대체 왜?’

고개를 돌려 주위를 둘러본다. 그러나 아무것도 보이지 않는다. 타들어 간 망막을 비롯한 감각의 상실은 그를 칠흑 같은 어둠 속에 가두었다.

다만, 아주 작은 소음만을 허락했을 뿐이었다.

……!

……!!

이상한 소리가 난다.

그래, 기억난다. 이건 비명과 강철의 마찰로 인한 소음이다. 

그리고 뒤이어 피부에 닿은 이 알 수 없는 무언가에게서는, 아주 친숙하면서 그리움이 느껴진다.

촤악.

그 순간, 잊고 있던 촉감과 기억이 깨어난다.

뜨겁고, 축축하며 끈적한 무언가.

더없이 익숙한 그것의 정체를 혈주는 떠올렸다.

‘피.’

인간의 몸 안에 존재하는 것. 자신에게는 힘의 원천이자, 지금의 이 갈증을 해소할 수 있는 유일한 액체.

‘목이 말라.’

희한한 일이다. 그렇게 생각하는 것만으로도, 전신 곳곳에 튄 핏물이 몸속으로 스며드는 것이 느껴졌다.

그에 힘입어, 점점 생생해지는 감각들도 함께.

그러나.

‘더. 더 줘.’

고작 이 정도로는 부족하다.

한참이나. 더욱더 많은 피가 필요했다.

“더!”

어느덧 흘러나온 외침과 함께, 혈주는 온 힘을 다해 손을 휘저었다. 

덥석.

마침내 손끝에 닿은 누군가의 어깨. 그와 동시에 조금 더 선명해진 목소리가 메아리처럼 귓가에 울려 퍼졌다.

“혈주시여! 속하들이 지켜드리겠……!”

하지만 그 다급한 음성이 끝맺어지기도 전, 어느덧 자라난 혈주의 이빨이 그의 목줄기를 깨물었다.

콰득!

씹고, 삼킨다.

더욱 큰 힘을 위해. 이 갈증을 해소하기 위해.

그제야 비로소, 괴물을 둘러싼 세상이 밝아졌다.
```

## Final English reading copy

```markdown
# Chapter 1108

He was dead.

No—he’d thought he was dead.

A quarter of an hour ago, the young man who had hurriedly thrown himself in front of Jin Taekyung, lost in a Trance and unable to sense the danger, had been certain he was about to die.

But he hadn’t.

After a blood-red flash charged with an unprecedented force came a tremendous impact that battered his entire body.

When he finally opened his eyes, clinging to the thread of consciousness that had briefly been severed, the young man buried beneath a pile of stones—or rather, Cheongpung—muttered to himself:

*This is the most dangerous thing I’ve ever been through… No, it isn’t.*

If this had happened before—or, more precisely, if he hadn’t gone through what happened on Mount Song—he might have trembled with fear.

Overwhelmed by the terror of death, something he’d never experienced before, and frozen by the killing intent and madness he’d never felt amid the clear streams and plum blossoms of Lotus Peak, he might have been unable to move.

But—

*I have to move.*

Things were different now.

The child who had wandered through Huashan’s beautiful scenery had entered the martial world and learned how to run.

He’d faced the world’s ugliness and learned what anger felt like. He’d spent time with good people and come to understand what human decency meant.

So even knowing that countless threats and hardships still lay ahead, he could rise again.

That was the right path his grandfather, who had raised him, had taught him. It was the chivalry he had learned from watching Jin Taekyung.

*Go. To my Benefactor. To them.*

Cheongpung pushed himself to his feet, unsteady.

He shoved aside the stones weighing down his body and endured the pain from bones broken here and there, moving slowly.

And more stealthily than ever before.

*“You want me to teach you martial arts?”*

Perhaps it was the blood trickling from the large and small wounds etched across his body. In his wavering vision, a conversation he’d once had with the Slaughter Saint seemed to echo in his ears.

*“Do you even know what you’re asking?”*

*“Uh, I think so.”*

*“Unbelievable. The Sword Saint’s Disciple, of all people, wants to become a mere assassin.”*

*“Huh?”*

*“You idiot. I don’t practice martial arts. I practice the art of killing. It’s not for someone like you.”*

Back then, the Slaughter Saint had shaken his head with a bitter smile.

At least, until he heard Cheongpung’s reply.

*“Huh. I don’t think that’s true.”*

*“What?”*

*“My grandfather told me it’s not the tool that matters, but the person holding it. And there was an assassin I saw a long time ago who didn’t seem like the kind of person who’d hurt someone for no reason.”*

*“……!”*

*“Oh, and he said everyone we cross paths with in this world could become our teacher and Benefactor.”*

*“……You.”*

*“Please take care of me, Granduncle!”*

Remembering how the Slaughter Saint had silently watched him, then spoken with an expression that grew complicated, Cheongpung let out a quiet breath.

*Hoo.*

His heart, pounding from pain and blood loss, grew calm. The blood flowing from wounds across his body gradually stopped, and his presence faded.

*“It won’t be easy to master even one technique. You don’t have the time, and the situation won’t allow for it.”*

*“Wow, so you’re saying yes, right? You are, aren’t you?”*

*“Damn it. Fine. But I have one condition.”*

*“A condition?”*

*“Never call me that again.”*

*“Yes, Little Master!”*

*“Damn it.”*

*“Oh. Sorry, Granduncle.”*

*“……Where in the world did the Sword Saint pick up a lunatic like you?”*

The Slaughter Saint probably hadn’t known.

Before even a month had passed since their journey began, he’d find himself asking that question again—but with a very different meaning.

*“……Where in the world did the Sword Saint pick up a lunatic like this?”*

*“Grandpa said a stork brought me. My Benefactor said it was something about ovulation, fertilization, and implantation, but I couldn’t make heads or tails of it.”*

*“……I really can’t understand.”*

*“Right? I’d never heard such bizarre words in my life.”*

*“……It’s my first time, too. Seeing a case this bizarre.”*

The Slaughter Saint’s bewildered face rose before Cheongpung’s eyes.

At the same time, his feet, now as light as feathers, touched a pool of blood.

No—they barely brushed it.

*Shhk.*

Ghost Illusory Slaughter Step.

The unique footwork technique created by the greatest assassin of all time—so stealthy that no other technique under heaven could match it—unfolded beneath Cheongpung’s feet.

*“You were right, Granduncle. This really isn’t easy.”*

*“……Is that something someone who reached three-tenths mastery in only a month should be saying?”*

It was the unique technique of none other than the Slaughter Saint, known as the greatest assassin of all time.

And yet Cheongpung had mastered Ghost Illusory Slaughter Step at a dazzling speed.

For someone else, a month might have been *only* a month. For him, it was an entire month.

*“I like martial arts. A whole, whole lot.”*

*“That much I know…… This is driving me mad. How is this even possible?”*

It was possible.

To Cheongpung, all of it came as naturally as breathing.

He watched with his eyes and moved with his body, and before he knew it, the technique became his.

Just as the words implied, it was reborn with Cheongpung’s own character woven into it—a new martial art that belonged to him alone.

*Whoosh.*

Cheongpung moved forward.

With each step, neither fast nor slow, it seemed that only he could smell the fragrance of plum blossoms spreading through the air.

Dark Fragrance Drift.

The fragrance of Huashan’s plum blossoms spread through the pouring rain. It had merged with Ghost Illusory Slaughter Step, which Cheongpung had brought to nine-tenths mastery over the past six months with the Slaughter Saint, becoming quieter and more elusive still.

So much so that even with both eyes open, no one could clearly make out his presence.

*Shh-shh-shh-shhk!*

“Graaagh!”

*Thrust! Slice!*

“Heaven above and earth below; all demons—Guh!”

The battle raging all around had already spun beyond anyone’s control, and yet no one noticed Cheongpung slipping past them.

As he crossed the heart of the battlefield, he blended naturally into everything around him.

He was the rain falling ceaselessly over everyone’s heads. He was one of Dark Heaven’s fanatics, drunk on madness and the effects of the Temporary Strength Pill—and one of the martial artists and soldiers trying to stop them.

He was a part of this chaotic battlefield, and the battlefield itself.

Moving in only one direction, toward only one person.

*Benefactor.*

Cheongpung saw him.

*Gooooom.*

The space warped as if gripped by an invisible hand. Jin Taekyung was about to unleash, all at once, an appallingly immense force.

And charging at him was the Blood Lord, while a pitch-black figure lunged from his blind spot, as though it had been waiting for this very moment.

*I’m too late.*

His instincts whispered.

It was a shame, but this wasn’t enough.

Cheongpung had neither the strength to bring down the Blood Lord nor the time.

But—

*He can do it. My Benefactor can.*

That wasn’t a guess. It was certainty.

An unwavering faith in Jin Taekyung.

So Cheongpung shot forward without hesitation.

Straight toward the enormous flames erupting in a distant flash of light.

Straight toward the Black Ghost, which had thrown its own body in the way as a shield to counter that unprecedented force.

*Fwoosh.*

Time slowed. Space disappeared.

Just before One Annihilation was unleashed, a flash of light slipped between his tightly shut eyelids and pierced his retinas like a needle.

But Cheongpung could feel it clearly.

The Black Ghost standing at the end of his path.

The strike he was making now, drawing a single line toward that pitiful figure.

And then—

*Shhk.*

The moment he passed the Black Ghost with a cut almost too quiet to hear, a lightning-like shiver surged up his spine.

A shiver that wouldn’t fade, not even in the dreadful heat swallowing the space he had just crossed.

*I did it.*

At the same time, a colossal fire dragon swallowed the Black Ghost’s body as it tilted helplessly.

No—or rather, it swallowed the blood-red monster charging from behind it.

*KWA-AAAAA!*

Even as the overwhelming shock wave swept him away, Cheongpung laughed aloud.

He watched the Red Blade shatter beneath the pillar of fire that had finally burst forth.

But he didn’t know.

At that very moment, one person was watching the blue-black flames dye everything around them.

Jin Taekyung’s face had gone colder than ever.

*Cough.*

His skin was deathly pale, his eyes growing cloudy.

Still, though he coughed up a whole bowlful of blood, Jin Taekyung forced his heavy eyelids open to watch the wave of fire he had unleashed.

He took in the clearest information in the world—the only information he could hear.

*Beep! Be-be-beep!*

He’d poured everything he had into it.

With a body emptied of strength and senses gone dry, he tried to understand what was happening.

But he couldn’t see or hear.

Not among the countless holographic windows floating in the air. Not amid the System warnings ringing without pause in his ears.

The clear chime announcing the enemy’s death never came.

Not even as his legs gave way, the spear shaft the only thing keeping him upright.

*Splash.*

And as Jin Taekyung’s knees plunged into a pool of blood—

*Drip. Drip.*

From within the wave of fire that had engulfed a radius of dozens of jang, the charred body of the monster stood up.

* * *

Thirst.

That was the first thing the Blood Lord felt when he regained consciousness.

*What the hell happened?*

He didn’t know. He couldn’t know.

He remembered nothing.

He couldn’t even recall who he was or what kind of life he’d lived.

Only the instinct to quench this terrible thirst remained, taking control of his body.

*Scuff.*

The sound of his unsteady footsteps was as dry as if he were walking through a desert.

Why was that?

The Blood Lord wondered blankly.

He’d been sure there was something somewhere around here that could quench his thirst.

He’d been sure of it.

*Why?*

He turned his head and looked around. But he couldn’t see anything. His senses had failed, his retinas burned away, trapping him in pitch-black darkness.

All he could make out was a faint sound.

……!

……!!

A strange noise.

Yes, he remembered. The sound of screams and steel clashing.

And then, from the unknown thing that touched his skin, came a feeling that was familiar—and strangely dear.

*Splash.*

At that moment, forgotten sensations and memories awoke.

Something hot, wet, and sticky.

The Blood Lord remembered what this utterly familiar thing was.

*Blood.*

Something inside the human body. The source of his strength—and the only liquid that could quench his thirst now.

*I’m thirsty.*

Strange. Just thinking it was enough for him to feel the blood splattered across his body seeping into him.

And with it, his senses gradually grew more vivid.

But—

*More. Give me more.*

This wasn’t nearly enough.

He needed far, far more blood.

“More!”

With the cry escaping his lips, the Blood Lord flung his hand out with all his strength.

*Grab.*

At last, his fingertips touched someone’s shoulder. At the same time, a voice rang more clearly in his ears, echoing like a distant sound.

“Blood Lord! We’ll protect you—!”

But before the desperate voice could finish, the Blood Lord’s teeth, already grown, sank into the man’s throat.

*Crunch!*

He chewed and swallowed.

For greater strength. To quench his thirst.

Only then did the world around the monster grow bright.
```
