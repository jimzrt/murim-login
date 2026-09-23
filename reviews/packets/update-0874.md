<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0874.txt",
      "sha256": "87277e9f5dfb12c6302d658f099a7bf127a42cd5461b8332d44ce5fc9b3d7119",
      "bytes": 14605
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6dd81a73c0bf4354531f31e9dde4a328d09aec1189ae3be109bf017a785ce7c0",
      "bytes": 1000
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a0000139fa1d2bae96120b59075e9f668e6032709b689eac2cb8719aefa088e0",
      "bytes": 230026
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "62dae01f7c8949a7b7f05b12fd52bb5370e6a5244156e12e837676f271d199d8",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "681452401a2fcd812211531c0932c6d0af41f3b4132aa66ff62ff084b5881acc",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "7c02bcaff55223ee284990d0d55e10ec3045ec9db6ae48653429f7a35c0b7c1f",
      "bytes": 854
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "73a3a79057aa96c63ab9b8920a693388f7b29ecb8e0caf0aa9e4aef6b122c1f1",
      "bytes": 1511
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "3ec77df84dc22cce48f798ed02f9679447c61ed30e60e6f109f218f3e913a395",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "d236324b1b2dd01df437b0ee105eecbc498871ab9aac4bd961fa8b78a840a60c",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "747f2b42f594e0c9f7fa0dba71a336918b1c226c9df72e6ab2a5948179aca6bf",
      "bytes": 257845
    }
  ],
  "estimated_tokens": 11392
}
-->

# Durable State Update — Chapter 874

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
1 and safe_through 874. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 874. Profile updates may replace only one
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
  "chapter": 874,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 874,
    "continuity_sources": [874],
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
    "The Emperor says he will take care of Prince Shangshan and proposes bringing him to the palace, away from his Shanxi posting.",
    "Taekyung argues that Shangshan is mature and independent; Shangshan calls Taekyung his guest and friend and begs for his life.",
    "The Emperor’s assassins have wounded Taekyung and are closing in. The Emperor permits a final farewell with Shangshan.",
    "First Shadow executed Third Shadow on the Emperor’s order after Third Shadow disobeyed him."
  ],
  "continuity_sources": [
    873
  ],
  "open_questions": [
    "What does the Emperor intend to do with Prince Shangshan in the palace?",
    "Can Taekyung protect Shangshan or escape the assassins?",
    "What will happen to Taekyung after the Emperor’s final offer?"
  ],
  "safe_through": 873,
  "temporary_decisions": [
    "Render 삼영 as “Third Shadow,” 일영 as “First Shadow,” and 관내후 as “Marquis Within the Passes.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 큰형     | **eldest brother**                           |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 삼영 | **Third Shadow** | Assassin named by the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 873
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 873
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 873
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 868
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 872
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 873
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃874화



결과는 일찍이 정해져 있던 것일지도 모른다.

완벽한 적지(敵地)라고 할 수 있는 황궁. 철통같다는 표현조차 부족할 만큼 삼엄한 경계. 그리고 온 천하의 지배자인 황제.

그 홀로 무대와 배우, 연출까지 모조리 도맡았으니 나라는 등장인물이 끼어들어도 상황은 크게 달라지지 않았을 것이다.

문득 그런 생각이 들었다.

어쩌면 이 모든 것이 황제에게 있어 일종의 유희였을 거라는 생각이.

구태여 만날 이유가 없는 나를 상산왕과 함께 부른 것도, 당장 역적으로 몰려도 이상하지 않을 말을 아무렇지 않게 넘어가는 것도.

거기에 더하여, 지금 이 순간 딱딱하게 굳어 버린 내 얼굴을 바라보며 조소(嘲笑)하는 것도.

우득.

힘껏 말아쥔 주먹에서 뼈 어긋나는 소리가 들렸다. 나는 새카만 복면 위로 드러난 살수들의 무감각한 눈동자를 훑으며 갈등했다.

‘어떻게 할까.’

황제의 이번 유희는 실로 대담하고도 자신만만했다.

당연하게도 모든 일행이 기존에 소지하고 있던 무기들은 황궁에 입성하며 진작 압수당했지만, 나를 향한 그 이상의 제재는 없었으니까.

천하의 그 누구도 황제인 자신을 해할 수 없다는 자신감일 수도 있다.

그러나 그런 황제의 선택은 명백한 실수였다.

제아무리 적수공권(赤手空拳)이라 해도 나는 중단전을 개방한 초인이자, 화왕 적천강으로부터 무시무시한 권장지공을 물려받은 열화문의 계승자였으니.

‘무기는 빼앗으면 그만.’

시선을 옮길 때마다 보이지 않는 나만의 길이 머릿속에 그려졌다.

가장 효율적이면서도 신속하게 살수들을 죽이고, 상산왕과 함께 이곳을 빠져나가는 길이.

황제가 초절정의 영역에 들어선 고수라는 사실은 예상 밖의 일이었으나 딱 거기까지였다.

‘아직은 초절정 초입. 만약 내가 팔 하나를 내줄 각오를 하고 황제부터 생포한다면?’

황제를 인질로 사로잡으면 모든 것이 끝난다. 대국은 하나의 거대한 기관 장치이고 황제는 그 중심에 있는 가장 중요한 부품이자 주인이니까.

그리고 그런 황제가 내 수중에 떨어진다면, 이 안의 살수들은 물론 밖에서 기다리고 있을 쌍둥이 고수까지 무력화시킬 수 있다.

어쩌면 금의위 지휘사 백연도.

‘하지만…… 그다음에는? 그다음은 어떻게 되는 거지?’

한번 시작하면 두 번 다시 돌이킬 수 없다. 그때부터는 진정한 반역의 시작이다.

만약 이대로 황제를 인질로 붙잡고 건청궁을 빠져나간다면, 마삼보가 이끄는 동창이 우릴 도울까. 그가 전날 밤 언급했던 연판장(連判狀)에 서명한 이들은 충분한 준비가 되었을까.

뒤죽박죽 뒤엉킨 뇌리에 갖가지 생각이 스쳐 지나가던 그때.

“신, 상산왕 주표. 지엄하신 형님 폐하의 뜻을 따르겠나이다.”

하나뿐인 친형이자 만인지상의 황제를 향해 깊게 절한 상산왕이 목청껏 외쳤다.

“만세. 만세. 만만세!”

“……!”

나도 모르게 가슴이 덜컥 내려앉았다.

상산왕이 보인 갑작스러운 행동에 전신을 옥죄고 있던 긴장감이 무너져서?

아니다.

가슴에도 닿지 않을 만큼 작은 저 어린 왕의 모습에서, 다급하면서도 절실한 뜻을 읽었기 때문이었다.

‘더는 나서지 마라.’

들을 수도 없고 들리지도 않는 그 목소리가 귓가에 울리는 듯했다.

지금 상산왕은 나를 만류하고 있었다. 돌이킬 수 없는 선택을 하기 전에 자신이 한발 앞서 나선 것이다.

그리고 그런 상산왕을 굽어보는 광오한 시선이 있었다.

“……확실히, 많이 컸군.”

미묘한 표정으로 중얼거린 황제가 소매를 내저었다. 만세를 외치며 연거푸 절하던 상산왕이 그 뜻을 알아차리고 자리에서 일어났다.

“정녕 내 뜻을 따르겠느냐?”

“물론입니다, 폐하.”

“네 뜻은 아니라는 말로 들리는구나. 원치 않는다면 거부해도 된다.”

말은 그렇게 해도 가늘게 뜨여진 황제의 눈은 다른 생각을 품고 있다.

그러나 묵묵히 고개 숙인 상산왕의 대답은 지금까지와 달리 침착하기 그지없었다.

“제 뜻이기도 합니다.”

“우리 형제의 뜻이 이토록 같다니, 짐은 기쁘기 한량없다.”

“황공하옵니다.”

이미 현실을 받아들인 듯 담담한 상산왕의 모습에 맥이 탁 풀린 나는 호흡을 가다듬었다.

‘틀렸어.’

상산왕의 선택이 옳았다.

이미 결론은 나왔다.

준비가 되지 않은 상황에서는 물러나야 한다.

‘적어도 오늘만큼은.’

그리고 그런 나를 바라보며 입맛을 다신 황제가 문득 입을 열었다.

“결정했다니 더는 긴말이 필요 없겠군. 알현은 이것으로 끝마치겠다. 모두 물러가라.”

“존명(尊命).”

죽은 삼영(三影)의 시신을 들쳐 업은 살수들이 어둠 속으로 녹아든 그때, 황제가 문득 덧붙였다.

“무영(無影). 그대도.”

스륵.

대답 대신 일렁이는 허공를 보며, 나는 입술 사이로 흘러나오려는 신음을 간신히 억눌렀다.

‘이런 미친.’

나조차도 기척을 파악하지 못한 초절정 고수.

아니, 정확히는 초절정의 살수.

아마도 황제가 나를 큰 제재 없이 자신의 처소에 들이고도 태연했던 이유는, 바로 그의 존재가 있었기 때문이었을 것이다.

‘끝까지 시험한 거였어, 나를.’

나는 황제에 대한 판단을 즉각 수정했다.

단순히 광오하고 대담한 것만이 아니다. 그는 누구보다 철두철미하면서도 의심이 많았다.

성공하면 황제요. 실패하면 역적이라.

내 생각이 너무나도 짧았다. 사황자라 불리던 시절의 그는 단 한 번 검을 뽑아 휘둘러 황도를 뒤엎고 대국을 손에 넣었다.

범인(凡人)은 꿈도 꿀 수 없는 과감함과 결단력.

만약 내가 움직였다면, 결코 살아서 건청궁을 빠져나가지 못했을 것이라는 생각이 문득 뇌리를 스쳤다.

‘빌어먹을.’

이게 황제의, 대국의 힘인가?

어린 왕을 지키기는커녕, 오히려 이렇게 힘없이 물러나는 것이 최선인가?

“가세.”

상산왕의 작은 중얼거림에, 나는 악문 잇새를 숨기기 위해 돌아섰다.

한바탕 유희를 끝마친 황제는 이미 하늘거리는 비단 사이로 자취를 감춘 후였다.

구구궁.

화려한 처소와는 어울리지 않는, 육중한 철문이 서서히 열렸다. 그리고 그 앞에는 오는 길에 보지 못했던 수십여 명의 궁인(宮人)들이 서 있었다.

“상산왕 전하를 뵈옵니다.”

“상산왕 전하를 뵈옵니다.”

지극히 공손한 태도로 상산왕을 향해 절하는 궁인들은 모두 빼어난 미인들이었다.

하나같이 경국지색(傾國之色)이라는 말이 어울릴 법한 수려한 용모의 소유자들.

하지만 그중에서도 한 걸음 앞으로 나와 있는 여인은 대번에 눈에 띄었다.

“소교(小嬌)라 불러 주시옵소서.”

소교. 그것이 여인의 이름이었다.

목소리는 차분하고 눈동자는 샛별처럼 반짝거린다. 이목구비의 아름다움을 따지기 이전에, 그녀에게는 묘한 느낌이 있었다.

“지엄하신 폐하의 명에 따라 상산왕 전하를 모시게 되었나이다. 앞으로는 천녀(賤女)들이 시중을 들 테니 심려 마소서.”

명색이 왕의 수행하는 이들임에도, 그들 중 중무장한 금의위의 모습이 보이지 않는 이유는 간단했다.

‘무공을 익혔군. 그것도 상당한 수준으로.’

하나같이 적정 수준의 공력을 갖춘 일류의 고수들.

더불어 나는 궁인들이 허리춤에 찬 저 얇은 요대가 연검(軟劍)이라는 사실을 즉각 알아차렸다.

만약 황제의 명령이 떨어지면, 언제든지 상산왕의 목을 파고들 것이라는 짐작도 함께.

‘시간이 없다.’

마음이 조급해진다. 한시라도 빨리 홍진을 만나 대비책을 세워야 한다. 황제가 감추고 있는 의중이 무엇인지, 그 흉계(胸悸)를 간파해야 했다.

“전하.”

내 부름에 상산왕이 고개를 들었다. 어린 왕은 체념인지, 혹은 침착인지 모를 담담한 눈빛으로 나를 바라보다 소교를 향해 입을 열었다.

“잠시 자리를 비켜 주었으면 하는데.”

건청궁에서 궁인으로 일한다는 것은 저들 역시 황제가 거느린 수많은 충복 중 하나라는 뜻.

그러나 소교는 잠시 생각하는 듯싶더니, 이내 조용히 궁인들을 이끌고 미로처럼 얽힌 복도를 지나 사라졌다.

그제야 상산왕 역시 애써 미소지을 수 있었다.

“말하게. 비록 우리가 언제 다시 만날지는 모르나, 긴 이별을 나누기에는 상황이 여의치 않음을 이해하게.”

일찍 철이 들어 버린 아이의 모습은 보는 이로 하여금 울컥하게 만드는 무엇인가가 있다.

하지만 감정에 휩쓸려서는 안 된다.

나는 목구멍까지 치고 올라온 말들을 꾹 눌러 삼키며 손을 내밀었다.

“우선 이것부터 받으십시오.”

“……?”

“어서요. 시간 없습니다.”

내 재촉에 잠시 머뭇거리던 상산왕이 이내 물건을 건네받았다.

그리고 손바닥에 놓인 작고 반짝이는 무언가를 확인하고 눈을 크게 떴다.

“이건…….”

“제 선물입니다.”

호기심 어린 눈빛으로 그것을 살피던 상산왕이 물었다.

“자네가 항상 끼고 다니던 바로 그 가락지로군.”

상산왕은 알 수도 없고, 짐작하지도 못하겠지만, 그것의 정확한 명칭은 바로 만독지환(萬毒指環)이었다.

사천당가의 신물이자 암천의 표적이 되었던 신병이기 중 하나.

그리고 평상시에는 인벤토리에 보관했던 백염이나 화룡갑과는 달리, 내가 만일을 대비해 언제나 끼고 있던 반지.

“이걸 갑자기 왜 과인에게?”

“전하께 필요할 것 같아서요. 황도에 오는 길에도 몇 번이나 관심 있게 보시지 않으셨습니까.”

사실이었다. 마차에 머무르는 시간은 길었고 상산왕은 내 모든 것에 관심을 가졌다.

이 시대의 여인들이 사용하기에는 너무 투박하고, 사내들이 착용하기에는 어색한 이 반지를.

심지어 며칠 전에는 만독지환을 자신에게 달라 조른 적도 있었다.



‘그 가락지 말인데.’

‘네? 아, 이거 말입니까.’

‘응. 그대가 낀 그 가락지. 혹시 과인에게 주지 않겠나?’

‘음. 죄송하지만 그건 좀 곤란한데요. 혹시 평소에도 치장에 관심이 있으셨습니까?’

‘아닐세. 그냥 자네 물건을 하나 갖고 싶어서.’

‘아, 애장품 수집…….’

‘뭐라고?’

‘아무것도 아닙니다. 그냥 혼잣말이었어요.’

‘여하튼 갖고 싶네. 물론 셈은 넉넉하게 치를 것이고.’

‘죄송합니다. 이건 누구한테 줄 수도 없고, 억만금을 줘도 못 팔아요.’

‘어째서? 과인의 부탁도 거절할 만큼 귀한 물건인가?’

‘그게 그러니까…… 그래. 아버지 유품이거든요.’

‘아.’

‘저뿐만 아니라 가문 전체에 의미가 깊은 물건입니다. 큰형님은 아직도 이 반지만 보면 눈물을 흘려요.’

‘자네 춘부장은 아직 살아 계시는 걸로 아는데.’

‘……생각해 보니 어머니 유품이었네요. 착각했습니다.’



만독지환은 애당초 다른 누군가의 손에 들어가서는 안 되는 물건이다.

결국 뜻을 이루지 못한 상산왕은 낙심했고, 나는 산서성으로 돌아가면 서명을 오천 장쯤 해 주기로 약속했다.

황도에서 어떤 일이 기다리고 있을지 윤곽도 그리지 못한 채로.

“이걸, 정말 과인에게 주겠다고?”

“아예 드리는 건 아닙니다. 나중에 반드시 돌려주셔야 해요.”

“어머니 유품이라고 하지 않았나?”

“어. 그러니까 그게…….”

내가 할 말을 잃어버린 그때, 상산왕이 피식 웃었다.

“이미 알고 있네. 그대가 거짓말을 했다는 것쯤은.”

“아.”

“과인에게까지 거짓을 고하다니, 조금 섭섭하긴 하지만 괜찮네. 무언가 그럴 만한 사정이 있겠지. 그만큼 귀중한 물건일 테고.”

나도 상산왕을 따라 미소지었다.

“맞습니다. 정말 귀한 거니까 항상 다른 사람 몰래 지니고 계시고…… 꼭 돌려주셔야 합니다.”

내 말에 담긴 의미를 모를 애늙은이가 아니다.

무슨 말을 해야할 지 모르는 사람처럼 머뭇거리던 상산왕이 크게 고개를 끄덕였다.

“응. 알겠네. 약속하지.”

그제야 나도 마음이 조금 놓였다.

이미 십여 년 전 역모를 통해 권좌에 오르며 무수한 비난과 암중의 적들을 만들어 낸 황제다.

상산왕을 황도까지 불러 손아귀에 넣을 만큼 명분을 중요시하는 황제가, 자신의 하나뿐인 동생을 죽이고자 한다면 가장 큰 가능성은 바로 독살(毒殺)이었다.

‘만독지환만 지니고 있다면 독살 가능성은 완전히 사라질 테고.’

그 틈에 시간을 벌어, 새로운 방법을 강구해 낸다.

내심 중얼거린 나는 저 멀리 천천히 되돌아오는 궁인들의 인기척을 느꼈다.

어느새 짧은 이별의 시간이 끝나가고 있었다.

“이만 가야 할 시간이로군.”

상산왕이 가라앉은 목소리로 중얼거린다. 나는 허리를 숙여 어린 왕과 시선을 맞추며 대답했다.

“금방 다시 만날 겁니다.”

“그러길 바라네. 그래야만 과인이 그대에게 진 빚을 갚을 수 있을 테니까.”

“전하.”

“응?”

“모르십니까? 친구 사이에는 빚 같은 거 없습니다.”

“……!”

“그래도 뭐, 굳이 주신다면 감사히 받고요.”

씩 웃은 나는 상산왕의 머리를 쓰다듬어 주었다.

눈을 동그랗게 뜬 채 나를 멍하니 바라보던 어린 왕도 따라 웃었다.
```

## Final English reading copy

```markdown
# Chapter 874

Perhaps the outcome had been decided long ago.

The imperial palace, a perfect enemy stronghold. A guard so tight that even “ironclad” didn’t do it justice. And the Emperor, ruler of all under heaven.

He alone had taken charge of the stage, the actors, and the direction. Even if I, a mere character, had entered the scene, the situation probably wouldn’t have changed much.

The thought came to me suddenly.

Perhaps all of this was a kind of amusement to the Emperor.

There was no particular reason to summon me along with Prince Shangshan. He’d brushed aside my words—words that could have gotten me branded a traitor on the spot—as if they were nothing.

And on top of that, he was now looking at my rigid face and sneering.

Crack.

A bone shifted with a sound from my tightly clenched fist. I scanned the impassive eyes visible above the assassins’ pitch-black masks, weighing my options.

*What do I do?*

The Emperor’s little game was daring—and supremely confident.

Naturally, all of us had been forced to surrender the weapons we’d brought into the palace. But beyond that, no restrictions had been placed on me.

Perhaps he was so confident that no one in the world could harm him, the Emperor.

But that choice had been an obvious mistake.

Even barehanded, I was a superhuman who had opened my Middle Dantian, an heir to the Fire Gate Clan who had inherited the Fire King Jeok Cheongang’s fearsome fist, palm, and finger techniques.

*All I have to do is take their weapons.*

With every shift of my gaze, an invisible path took shape in my mind.

A path to kill the assassins as quickly and efficiently as possible, then escape with Prince Shangshan.

The fact that the Emperor was a master who had entered the realm of Supreme Peak was unexpected, but that was all.

*He’s still at the threshold of Supreme Peak. What if I’m willing to sacrifice an arm and capture the Emperor first?*

If I took the Emperor hostage, it would all be over. The Great Nation was one enormous mechanism, and the Emperor was its most important component—and its master.

And if the Emperor fell into my hands, I could neutralize not only the assassins in here but also the twin masters waiting outside.

Perhaps even Baek Yeon, Commander of the Embroidered Uniform Guard.

*But… what then? What happens after that?*

Once I started, there would be no going back. That would be the beginning of a true rebellion.

If I took the Emperor hostage and fled Qianqing Palace, would the East Depot, led by Ma Sanbao, help us? Were the people who had signed the collective pledge he’d mentioned the night before fully prepared?

As all kinds of thoughts tangled through my mind—

“Your servant, Prince Shangshan Zhu Bao, will obey the will of my most august elder brother, Your Majesty.”

Prince Shangshan bowed deeply before his one and only elder brother, the Emperor and the highest person under heaven, then cried out at the top of his voice.

“Long live the Emperor! Long live the Emperor! Long, long live the Emperor!”

“……!”

My heart lurched.

Was it because Prince Shangshan’s sudden action broke the tension that had been squeezing my whole body?

No.

In the sight of that young prince, so small he couldn’t even reach my chest, I read a desperate, urgent plea.

*Don’t step in any further.*

It was as if a voice I couldn’t hear, a voice that couldn’t be heard, had sounded in my ear.

Prince Shangshan was trying to stop me. Before I could make an irreversible choice, he’d stepped forward first.

And an arrogant gaze looked down at him.

“……You’ve certainly grown.”

The Emperor murmured, his expression hard to read, and swept his sleeve. Prince Shangshan, who had been crying “Long live” and bowing again and again, understood and rose to his feet.

“Do you truly intend to obey my will?”

“Of course, Your Majesty.”

“That sounds like you’re saying it isn’t your own will. You may refuse if you don’t want to.”

The Emperor said that, but his narrowed eyes held another thought.

Prince Shangshan bowed his head in silence. Unlike before, his answer was utterly calm.

“It is my will, too.”

“I’m overjoyed that my brother and I are so much of one mind.”

“I am deeply honored.”

Prince Shangshan seemed to have accepted reality. At the sight of his calm expression, the tension drained out of me. I steadied my breathing.

*It’s no good.*

Prince Shangshan had made the right choice.

The conclusion was already clear.

We had to retreat when we weren’t prepared.

*At least for today.*

The Emperor watched me and smacked his lips, then suddenly spoke.

“Now that you’ve decided, there’s no need for further discussion. This audience is over. Everyone, withdraw.”

“As Your Majesty commands.”

As the assassins picked up Third Shadow’s body and melted into the darkness, the Emperor added,

“No Shadow. You too.”

Shff.

I barely held back a groan at the sight of the air rippling in place of an answer.

*This is insane.*

A Supreme Peak master whose presence even I hadn’t sensed.

No—not quite. A Supreme Peak assassin.

That was probably why the Emperor had been so untroubled about letting me into his chambers without imposing any serious restrictions.

*He’d been testing me to the very end.*

I revised my judgment of the Emperor at once.

He wasn’t merely arrogant and daring. He was more meticulous and suspicious than anyone.

*If you succeed, you’re the Emperor. If you fail, you’re a traitor.*

I hadn’t thought it through. When he was still known as the Fourth Prince, he’d drawn his sword just once, swung it, and overturned the imperial capital to seize the Great Nation.

A boldness and decisiveness no ordinary person could even dream of.

The thought suddenly crossed my mind: if I’d made a move, I would never have left Qianqing Palace alive.

*Damn it.*

Was this the power of the Emperor? The power of the Great Nation?

Was my best option really to withdraw so helplessly, unable even to protect a young prince?

“Let’s go.”

At Prince Shangshan’s quiet murmur, I turned away to hide my gritted teeth.

The Emperor, having finished his little game, had already disappeared behind the fluttering silks.

Rumble.

A massive iron door, ill-suited to such a splendid chamber, slowly opened. Standing beyond it were dozens of palace attendants I hadn’t seen on the way in.

“We greet His Highness Prince Shangshan.”

“We greet His Highness Prince Shangshan.”

The attendants bowed to Prince Shangshan with utmost deference. Every one of them was a striking beauty.

Each had the kind of exquisite looks that could topple kingdoms.

But one woman standing a step in front of the rest immediately caught my eye.

“Please call me So Gyo.”

So Gyo. That was the woman’s name.

Her voice was calm, and her eyes sparkled like morning stars. Even before you considered the beauty of her features, there was something unusual about her.

“By His Majesty’s solemn command, we have been assigned to serve His Highness Prince Shangshan. From now on, we humble women will attend to you, so please do not worry.”

It was simple enough to understand why none of them were heavily armed Embroidered Uniform Guards, despite being assigned to accompany a prince.

*They’ve trained in martial arts. And at a considerable level, too.*

Every one of them had the internal energy of a First Rate master.

I also immediately recognized that the thin belts at their waists were flexible swords.

And I couldn’t help guessing that if the Emperor gave the order, they’d be ready to drive those blades into Prince Shangshan’s neck at any moment.

*There’s no time.*

I was getting anxious. I had to meet Hong Jin as soon as possible and make a plan. I had to see through the Emperor’s hidden intentions, to discern his scheme.

“Your Highness.”

Prince Shangshan lifted his head at my call. The young prince looked at me with a calm gaze that might have been resignation, or composure, then turned to So Gyo.

“I’d like you to give us a moment.”

Working as a palace attendant in Qianqing Palace meant that they, too, were among the Emperor’s many loyal servants.

But So Gyo seemed to consider it for a moment, then quietly led the attendants away down the maze of corridors.

Only then could Prince Shangshan manage a faint smile.

“Speak. Though we may not meet again for some time, understand that the circumstances aren’t right for a long farewell.”

There was something about a child forced to grow up too soon that brought a lump to your throat.

But I couldn’t let my emotions take over.

I swallowed the words rising to my throat and held out my hand.

“First, take this.”

“……?”

“Come on. There’s no time.”

Prince Shangshan hesitated at my urging, then accepted the object.

He looked down at the small, glimmering thing in his palm and his eyes widened.

“This is…”

“My gift to you.”

Prince Shangshan examined it curiously, then asked,

“That’s the very ring you always wear.”

Prince Shangshan couldn’t know—and had no reason to guess—that its proper name was the Myriad-Poison Ring.

A divine artifact of the Sichuan Tang Clan, and one of the divine weapons Dark Heaven had targeted.

Unlike White Flame and Fire Dragon Armor, which I usually kept in my Inventory, this was a ring I wore at all times, just in case.

“Why would you suddenly give this to me?”

“I thought you might need it, Your Highness. You’ve shown an interest in it several times on the way to the imperial capital.”

That was true. We’d spent a long time in the carriage, and Prince Shangshan had been curious about everything I owned.

Even this ring, too clunky for the women of this era and awkward for a man to wear.

A few days ago, he’d even pestered me to give it to him.

*“About that ring.”*

*“Hm? Oh, this one?”*

*“Yes. The one you’re wearing. Would you give it to me?”*

*“Um, sorry, but that’s a little difficult. Have you always been interested in accessories?”*

*“No. I just want something of yours.”*

*“Oh, collecting keepsakes…”*

*“What was that?”*

*“Nothing. Just talking to myself.”*

*“At any rate, I’d like to have it. Of course, I’ll pay you handsomely.”*

*“I’m sorry. I can’t give this to anyone, and I couldn’t sell it for any amount of money.”*

*“Why not? Is it so precious that you’d refuse even my request?”*

*“Well, you see… Right. It was my father’s keepsake.”*

*“Oh.”*

*“It’s important not only to me, but to the whole family. My eldest brother still cries whenever he sees this ring.”*

*“I believe your father is still alive.”*

*“……Now that you mention it, I think it was my mother’s keepsake. I was mistaken.”*

The Myriad-Poison Ring was never supposed to end up in anyone else’s hands.

In the end, Prince Shangshan had been disappointed, and I’d promised to sign about five thousand autographs when we returned to Shanxi Province.

That was before I had the faintest idea what might be waiting for us in the imperial capital.

“Are you really giving this to me?”

“I’m not giving it to you for good. You have to return it later.”

“Didn’t you say it was your mother’s keepsake?”

“Uh. Well, you see…”

Just as I ran out of things to say, Prince Shangshan let out a quiet laugh.

“I already know you were lying.”

“Ah.”

“I’m a little disappointed that you’d lie even to me, but it’s all right. You must have had a reason. It must be that precious.”

I smiled along with Prince Shangshan.

“That’s right. It’s very precious, so keep it hidden from other people at all times…and make sure you return it.”

He wasn’t a precocious old soul for nothing. He understood the meaning behind my words.

Prince Shangshan hesitated, as if he didn’t know what to say, then nodded firmly.

“Mm. I understand. I promise.”

Only then did I feel a little more at ease.

The Emperor had ascended to the throne through a coup more than a decade ago, making countless enemies in the shadows and earning no shortage of blame.

The Emperor cared enough about having a legitimate pretext to summon Prince Shangshan to the imperial capital before bringing him under his control. If he meant to kill his one and only younger brother, the most likely method was poison.

*If Prince Shangshan keeps the Myriad-Poison Ring on him, poisoning him won’t be an option.*

That would buy me some time to come up with another plan.

I murmured to myself as I sensed the palace attendants slowly returning from farther down the corridor.

Our brief farewell was almost over.

“It’s time for me to go.”

Prince Shangshan murmured in a subdued voice. I bent down to meet the young prince’s eyes and answered,

“We’ll meet again soon.”

“I hope so. Then I’ll be able to repay the debt I owe you.”

“Your Highness.”

“Yes?”

“Don’t you know? Friends don’t owe each other anything.”

“……!”

“Still, if you insist on giving me something, I’ll accept it gratefully.”

Grinning, I ruffled Prince Shangshan’s hair.

The young prince stared blankly at me with wide eyes, then smiled, too.
```
