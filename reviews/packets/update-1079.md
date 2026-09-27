<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1079.txt",
      "sha256": "c4062fbf21f50457dd91387ceb940a868d4dae69fe63e476d7c070fe6fe51596",
      "bytes": 11726
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "01e923f2c193c50ee0f20e5dfe835826e8523083700c64ae9e9d42984b59cd53",
      "bytes": 952
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9a8d720626806d2f1522c18896823846cfaaacc04c6179a6dbd0fcad499df6e0",
      "bytes": 242769
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c3395c15aeb464040ab3e8cc7562b739bf1e368ffe58dd4cb3928f6c4ae8276c",
      "bytes": 1115
    },
    {
      "path": "characters/Hak Su.md",
      "sha256": "1ff392ea31933cf8d6c4d096e68f030a3b4e5e92d70bcebbe453c262b383d77e",
      "bytes": 615
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "53d032bd53e82e8e26c9559a75b1add9e1c930af40e491ff14933803d1886bec",
      "bytes": 1375
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5503698458aabb9e4b90a25bde172e935d8d07b03b9fc541eaf409361b0a9923",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2b2b70b92551c53154dd62e33de7133619cc0892d397ea04297a9c2958db27cf",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "64aed7776995e97697d3df7399bc7971af9cae5f595449f0efd71bddc0765629",
      "bytes": 285915
    }
  ],
  "estimated_tokens": 9598
}
-->

# Durable State Update — Chapter 1079

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
1 and safe_through 1079. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1079. Profile updates may replace only one
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
  "chapter": 1079,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1079,
    "continuity_sources": [1079],
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
    "The allies are crossing Qinghai Lake by ship and expect to reach their destination in about half a day.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to the Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive is being interrogated after a day and night submerged in the lake; he has promised to talk but has given no information."
  ],
  "continuity_sources": [
    1077,
    1078
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?"
  ],
  "safe_through": 1078,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 소생      | **I**; occasionally “this humble one” in highly formal dialogue |
| 소협      | **Young Hero**                                                  |
| 학수 | **Hak Su** | Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 학수 | 진태경 | Kunlun Senior Disciple to visiting martial artist | Fellow Daoist Jin | polite and respectful | Addresses Taekyung as 진 도우. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1076
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival, and the Slaughter Saint has become his mentor in concealment.

### Hak Su.md

# Hak Su (학수)

- **Safe through:** Chapter 1078
- **Aliases:** None
- **Role:** Hak Su is Cheongheoja’s Senior Disciple and a senior brother to Hak Woo in the Kunlun Sect.
- **Personality:** Gracious and hopeful, he responds to Taekyung’s mistakes with patience and warmth.
- **Voice:** He speaks in courteous, formal phrases and tempers earnest reassurance with hearty, lightly humorous remarks.
- **Relationships:** Cheongheoja is his Master, and Hak Woo is his youngest Junior Brother; he treats Jin Taekyung warmly as a Fellow Daoist.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1078
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1078
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1078
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1079화




누군가가 꼬박 하루 밤낮하고도 반나절 동안 수백 번도 넘게 강물에 처박히고도 살아남을 수 있느냐 묻는다면, 나는 단호하게 대답할 것이다.

당연히 살 수 있다고.

그리고 거기에 더해, 그 전과는 비교도 되지 않는 진실성을 얻을 수도 있다고.

물론, 그 과정에서 약간의 애로사항이 생길 수는 있겠지만.

“흐으, 흐으으…….”

“조장님. 이놈 이거 눈이 완전히 풀렸는데요?”

“풀렸으면 다시 조여야지.”

“어떻게요?”

“귀싸대기 한 대 올려붙여. 시원하게.”

“아하.”

큰 깨달음을 얻은 듯한 표정으로 고개를 끄덕인 혁무진이 냉큼 손바닥을 치켜세웠다.

짝!

“안 깨어나는데요?”

“너 바보냐?”

“왜요?”

“더 세게 쳐야지. 일어날 때까지.”

“오. 천재십니까?”

“천재까지는 아니고. 수재 정도.”

“역시.”

탄성을 터트린 혁무진이 이번에는 양손을 번쩍 쳐들었다.

짝! 쫙! 쫘악!

“어어, 이놈 눈깔 뒤집혔습니다.”

“엄살이야.”

“아니, 농담이 아니에요. 몸도 완전히 얼음장입니다.”

“어라, 진짜네.”

“그렇다니까요.”

“이 새끼 이거 마음이 차가워서 그래.”

“지금 그런 실없는 소리를 하실 때가 아닙니다. 이러다가 죽으면 어떡해요?”

“안 죽어. 마음이 따뜻한 내가 있잖아.”

“예?”

혁무진이 이 병신은 또 무슨 헛소리를 하는 거지, 라는 표정으로 쳐다본 순간. 나는 망설임 없이 손을 뻗었다.

퍼엉!

열양지기(熱陽之氣)가 담긴 뜨끈한 일장이 가슴팍에 적중하자, 창백하게 굳어 가던 흑의인의 신형이 부르르 떨리더니 이내 전과는 비교할 수 없는 온기를 띄었다.

“……와, 이걸 사네.”

“말했지. 나는 마음이 따뜻하다고.”

“이건 마음이 아니라 공력이 따뜻한 거 아닙니까?”

“너도 얘처럼 따뜻해져 볼래? 지금 좀 추워 보이는데.”

“죄송하지만 그건 정중하게 사양하겠…….”

으득!

“헉!”

“왜?”

“놈이 혀를, 혀를 깨물었습니다! 피가 엄청 나와요!”

“얼씨구. 지랄 났네, 아주.” 

“그러게 아혈(啞穴)은 풀지 말라고 말씀드렸잖아요! 아무리 공력이 금제 되어 있어도 지금 같은 상황이면 죽을 수도 있다니까요!”

“아혈까지 점해 놓으면 말 한마디 못한 채로 물귀신 될까 봐 그랬지. 여하튼 난리 그만 피우고 후딱 가서 모셔와.”

“모셔와요? 누구요?”

“누구겠냐?”

“아.”

그리고 잠시 후, 살수와 의원이라는 전혀 상반된 두 직종에서 달인의 경지에 도달한 프로 투잡러는 갑작스럽게 발생한 응급환자를 눈 깜짝할 사이에 소생시켰다.

“봉합까지 완벽하게 해 두었으니 회복 후 말하는 데에도 전혀 지장 없을 거다.”

“감사합니다.”

“헌데 이놈, 설마 내가 아는 그놈이냐?”

“예. 지난번에 데려오신 그놈이요.”

“몸뚱어리가 하도 퉁퉁 불어서 하마터면 못 알아볼 뻔했군. 저놈은 손목의 상처도 덜 나았으니 적당히 해라. 상처의 감염으로 괴사(壞死)라도 일어나면 큰일이니.”

“아, 그건 제 몸이 아니라서 괜찮습니다.”

“그것도 그렇군. 하지만 계속해서 무식하게 다루다 보면 목숨을 잃기 십상이다. 차라리 이럴 때는 경추(頸椎)에서 세 마디 아래쪽에서 깊게 찌른 다음 천천히…….”

“오, 그런 방법이. 그런데 이 정도면 죽지 않을까요?”

“죽지는 않고, 죽고 싶어 하긴 하더군.”

인체의 분해와 치료로는 천하에서 둘째가라면 서러운 전문가가 개꿀팁을 전수해 주고 떠나자, 이 모든 광경을 눈앞에서 지켜본 흑의인의 신형이 요동쳤다.

“읍. 으읍…….”

“어허, 얘가 갑자기 또 왜 이래. 좀 가만히 있어 봐.”

“으으읍……!”

“안 되겠다. 무진아.”

“예.”

“좀 잡고 있어 봐라. 연습 좀 하려는데 자꾸 떨려서 쉽지 않네. 점혈을 해 놨는데도 이 정도면 얼마나 몸부림을 치는 거야?”

“이런 건방진 자식이 지금 조장님 연습하시겠다는데. 영차, 이 정도면 됩니까?”

“그래. 딱 좋네. 그럼 찌른다?”

“잠깐만요. 그런데 그 위치가 맞습니까?”

“맞지 않냐? 경추에서 두 마디 아래쪽부터 시작이라고 들은 것 같은데.”

“어라, 위쪽으로 두 마디 아니었어요?”

“그럴 리가. 여기는 사혈(死血)인데?”

“헷갈리네요. 그냥 조장님께서 다시 가서 여쭤보시죠?”

“왜 내가 가? 네가 가야지.”

“제가 가면 죽을 수도 있잖아요. 가뜩이나 두 번 말하는 거 엄청 싫어하시는 분인데.”

“내가 가면 다를 것 같냐?”

“그것도 그러네요. 그냥 두 곳 다 찌르시죠?”

“그거 괜찮네. 그럴까 그럼?”

“옙. 가시죠.”

“으으읍! 으으으읍!”

드드득!

과장 조금 보태서, 이제는 지진이라도 난 것처럼 흔들리는 갑판.

점혈을 해 두었음에도 불구하고 온 힘을 다해 몸부림치는 흑의인의 모습에, 나는 내심 피식 웃으며 아혈을 풀어 주었다.

“푸하! 콜록, 콜록!”

“왜, 마지막이라도 남길 말이라도 있어?”

“세, 세 마디.”

“응?”

“경추! 경추에서 아래쪽으로 세 마디라고! 그만해 이 미친놈들아!”

상대가 손만 까딱하면 목숨을 잃을 수도 있는 상황에서, 미친놈 운운할 수 있는 경우는 단 두 가지뿐이다.

첫째, 죽음을 각오했거나.

둘째, 그런 것 따위는 이제 안중에도 없을 만큼 이성적인 판단이 불가능하거나.

그리고 놈은 명백한 후자였다.

‘끝났군.’

오직 공포로 가득 차 있는 그 눈빛과 음성을 본 순간, 나는 놈이 매우 진실 된 인간으로 새롭게 거듭났음을 깨닫고 자리에서 일어났다.

“어? 안 찌르시게요?”

“찌르긴 뭘 찔러. 우선 몸 덮을 것 좀 주고, 옆에 딱 달라붙어서 얘기나 나눠 봐.”

“조장님은요?”

“지금부터 다른 일로 좀 바빠질 것 같아서, 안 그렇습니까?”

내가 불쑥 던진 물음에, 귀신이라도 본 듯한 얼굴로 일련의 상황을 지켜보던 학수가 침을 꿀꺽 삼켰다.

“무, 무슨 말씀이신지.”

“아, 생각해 보니 아직 못 보시겠구나. 저쪽이요.”

내가 손을 들어 뱃머리 너머를 가리킨 그때.

화아악.

자욱한 물안개가 걷히며, 그 뒤에 가려져 있던 녹음(綠陰)의 대지가 모습을 드러냈다.

그곳에서 우리를 기다리기 위해 선착장에 모여있는 일단의 무리와 그런 그들의 어깨너머로 저 멀리 희미하게 보이는 회색 성벽도 함께.

청해성의 수도이자, 암천과 맞설 최후의 보루.

‘저곳이 바로, 서녕(西寧).’

그 순간.

띠링.

빠르게 갈라지는 강물 위로, 맑은 종소리가 울려 퍼졌다.



* * *



환영 인파는 실로 엄청났다.

아니, 거대하다고 표현하더라도 조금도 어색하지 않을 정도였다.

“와아아아아!”

“지원군이다! 무림맹의 지원군이 왔다!”

교과서에서나 보던 로마제국의 개선식이 이랬을까.

성벽에 가까워질수록 커져 가던 함성은 입성(入城)과 동시에 온 사방을 떨어 울렸고, 시야에 닿는 곳 어디든 새카맣게 몰려든 군중들로 가득했다.

넓게 펼쳐진 대로와 비좁은 골목길은 물론이요, 줄줄이 늘어선 누각(樓閣)을 비롯한 수많은 건물의 지붕 위까지 차지한 그들은 우리를 향해 두 팔을 뻗은 채 환호를 보냈다.

오죽하면 어지간한 관심종자인 청풍조차 마른침을 꿀꺽 삼키며 이렇게 속삭일 정도였다.

“조금만 더 있다가는 귀청이 터질 것 같아요, 은인.”

“그래?”

“예, 농담이 아니라 정말로요. 이렇게 요란한 소리는 처음 들어 봐요.”

“거울 치료 성능 확실하네.”

“네? 거울 치료가 뭐예요?”

“그러니까 그게…… 아니다. 알아봤자 청 소협은 달라지지 않을 거야.”

평상시였다면 순수한 광기로 무장한 채 거울 치료의 뜻을 캐물었을 청풍이었지만, 이번만큼은 조용히 속삭임을 이어 갔다.

“사람들이 엄청 많아요. 진짜 엄청이요. 잠깐 서녕에 머무른 적이 있긴 하지만 그때는 이 정도는 아니었는데.”

나와 달리 앞서 청해성에 한 달 정도를 머물렀던 청풍이니, 이와 같은 변화가 더욱 크게 느껴지는 모양이다.

물론 이 엄청난 숫자의 인파가 어디에서 왔는지, 나는 이미 짐작하는 바가 있었지만.

‘청해성 곳곳에 흩어져 있던 사람들이 전부 서녕으로 모여든 거겠지.’

당연한 결과다.

이보다 앞서 산서에서, 그리고 감숙에서도 이와 같은 상황이 벌어졌으니까.

이미 대국 황실은 암천을 역적이자 외적(外敵)으로 선포했고, 이와 같은 조치는 아직 안일한 생각을 품고 있는 백성들에게 경각심을 심어 주기 위해서는 필수적이었다.

막상 민초들에게는 별다른 피해가 가지 않았던 정마대전(正魔大戰)때와는 달리, 암천의 행보는 무림의 울타리를 아득히 벗어난 지 오래니까.

과거의 천마(天魔)가 노린 것이 천하 무림이었다면, 지금의 천주는 천하 그 자체를 노린다.

아니.

‘어쩌면 그 이상을.’

시간이 흐를수록 선명해져만 가는 불안감의 실체를, 나는 애써 억누르며 입꼬리를 말아 올렸다.

지금 이 순간에도 끝없이 사방을 뒤덮은 저 수많은 인파가 내 웃음을 보고 조금이라도 안심할 수 있도록.

“열화신룡 진태경이다!”

“상산후께서 오셨다!”

“와아아아! 대국 만세! 황제 폐하 만세!”

아무리 머릿수가 많다고 하나, 어차피 저들 중 대부분은 무림의 사정에 그리 밝지 않은 백성들이다.

저들의 눈에 비친 나는 단순히 젊은 무림인이 아니라, 천자의 지엄한 황명을 받들어 외적을 토벌하고 자신들을 구원하러 온 신장(神將)이나 다름없는 상황.

확연하게 커지는 함성소리에 청풍이 눈을 동그랗게 떴다.

“와아, 다들 은인을 좋아하나 봐요.”

내심 쓴웃음을 삼킨 내가 낮은 목소리로 대답했다.

“그래 보이긴 하네. 적어도 아직까지는.”

“분명히 앞으로도 그럴 거예요. 은인은 그만큼 좋은 사람이니까!”

“좋은 사람이라…….”

나는 말꼬리를 흐리며 성내를 꽉 채운 환영 인파를 바라보았다.

얼핏 보기에도 물경 수십만. 

혹은 그 이상이라 해도 과언이 아닐 무수한 사람들.

지금 이 순간 저들은 밝게 웃으며 내게 환호를 쏟아내고 있지만, 과연 언제까지 저 웃음이 입가에 남아있을지는 나로서도 알 수 없었다.

만약, 정말 만에 하나 최악의 사태가 벌어진다면 이 많은 사람 중 몇이나 살아남을 수 있을지조차.

“청 소협.”

“네?”

“네?”

“해보자. 우리가 할 수 있는 데까지.”

나는 인파를 바라보며 조용히 덧붙였다.

“목숨을 걸고.”

그래.

언제나 그래 왔듯이.
```

## Final English reading copy

```markdown
# Chapter 1079

If someone asked me whether a person could survive being dunked in a river hundreds of times over the course of a full day and night—and half a day on top of that—I’d answer without hesitation:

Of course they could.

And they might even gain a level of honesty that put their previous self to shame.

Naturally, there might be a few minor complications along the way.

“Ugh… ugh…”

“Captain, this guy’s eyes are completely glazed over.”

“If they’ve gone slack, we’ll just have to tighten them up again.”

“How?”

“Give him a good slap across the face. Nice and hard.”

“Ah.”

Hyuk Mujin nodded as if he’d just reached a great insight, then promptly raised his palm.

*Smack!*

“He’s not waking up.”

“Are you stupid?”

“Why?”

“You have to hit him harder. Until he wakes up.”

“Oh. Are you a genius?”

“Not a genius. Just exceptionally gifted.”

“Figures.”

Mujin gasped in admiration and raised both hands this time.

*Smack! Smack! Smack!*

“Uh, his eyes rolled back.”

“He’s exaggerating.”

“No, I’m serious. His body’s completely ice-cold, too.”

“Huh. So it is.”

“I told you.”

“This bastard’s cold because his heart is cold.”

“Now is not the time for nonsense. What if he dies?”

“He won’t. I’m here, and my heart’s warm.”

“What?”

The moment Mujin looked at me as if to say, *What kind of bullshit is this idiot talking about now?* I reached out without hesitation.

*Boom!*

When my palm, warmed by Scorching Yang Qi, struck his chest, the black-robed man’s body—which had been turning pale and rigid—shuddered. Then warmth returned to him, more than before.

“…Wow. He actually survived.”

“Told you. I have a warm heart.”

“Isn’t it your internal energy that’s warm, not your heart?”

“Want to warm up like him? You look a little cold.”

“I must politely decline…”

*Crack!*

“Gah!”

“What?”

“He bit his tongue! There’s so much blood!”

“Good grief. What a mess.”

“I told you not to release his Mute Acupoint! Even with his internal energy sealed, he could die in a situation like this!”

“If I’d sealed his Mute Acupoint, he might’ve drowned without getting a word out. Anyway, quit making a fuss and go fetch him.”

“Fetch who?”

“Who do you think?”

“Oh.”

A moment later, a professional two-jobber who had reached the peak of his craft in two completely opposite professions—assassin and physician—revived the emergency patient in the blink of an eye.

“I stitched him up perfectly, so he’ll have no trouble speaking once he recovers.”

“Thank you.”

“But this man—is he the one I’m thinking of?”

“Yes. The one you brought in last time.”

“He was so bloated I nearly didn’t recognize him. His wrist wound hasn’t healed yet, either, so don’t overdo it. If the wound gets infected and turns necrotic, you’ll be in trouble.”

“Oh, it’s not my body, so that’s fine.”

“True enough. But if you keep handling him so roughly, he’s liable to lose his life. In a situation like this, you’re better off stabbing him deeply three vertebrae below the cervical vertebrae, then slowly…”

“Oh, that’s a handy tip. But wouldn’t that kill him?”

“He wouldn’t die. He’d just wish he had.”

The expert, second to none in the world when it came to taking apart and treating the human body, passed on his useful tip and left. The black-robed man, who had watched the whole thing unfold right before his eyes, began to thrash.

“Mmph! Mmmph…”

“Hey, why are you acting up again? Just stay still.”

“Mmmph!”

“Can’t be helped. Mujin.”

“Yes, sir.”

“Hold him down for a bit. I’m trying to practice, but it’s hard when he keeps shaking. I used a Pressure-Point Strike, and he’s still struggling this much. How badly is he thrashing around?”

“This insolent bastard. The Captain’s trying to practice here. Heave-ho. Is this good?”

“Yeah. Perfect. All right, I’m going to stab him.”

“Wait. Are you sure that’s the right spot?”

“Isn’t it? I thought I heard it started two vertebrae below the cervical vertebrae.”

“Huh? Wasn’t it two vertebrae above?”

“No way. That’s a lethal acupoint.”

“I’m confused. Shouldn’t you go ask him again, Captain?”

“Why should I go? You go.”

“I could die if I go. And he hates having to repeat himself.”

“You think it’d be any different if I went?”

“Fair point. How about stabbing both spots?”

“That’s not a bad idea. Shall we?”

“Yes, sir. Go ahead.”

“Mmmph! Mmmmmmph!”

*Rrrrrumble!*

The deck shook as if an earthquake had hit—though that might be a slight exaggeration.

The black-robed man thrashed with all his might despite the Pressure-Point Strike. I let out a quiet laugh to myself, then released his Mute Acupoint.

“Gah! Cough, cough!”

“What is it? Got any last words?”

“Th-three vertebrae.”

“Hm?”

“Cervical vertebrae! Three down from the cervical vertebrae! Stop it, you madmen!”

There are only two reasons someone might call you a madman when you could take their life with the slightest movement of your hand.

First, they’ve resigned themselves to death.

Second, they’re no longer capable of rational thought, to the point where they don’t care about something like that.

He was clearly the latter.

*It’s over.*

The terror in his eyes and voice told me he had been reborn as a far more honest man. I stood up.

“Huh? You’re not going to stab him?”

“Why would I stab him? Get something to cover him with, then sit right beside him and have a chat.”

“What about you, Captain?”

“I’m about to get busy with something else. Isn’t that right?”

At my sudden question, Hak Su—who had been watching the whole scene with the face of a man who’d seen a ghost—swallowed hard.

“I-I’m not sure what you mean.”

“Oh, right. You can’t see it yet. Over there.”

Just as I raised my hand and pointed beyond the bow—

*Whoosh.*

The thick fog lifted, revealing the lush green land hidden behind it.

A group of people had gathered at the pier to welcome us. Over their shoulders, far in the distance, the gray walls of a city were faintly visible.

Xining, the capital of Qinghai Province and the last stronghold against Dark Heaven.

*That’s Xining.*

At that moment—

*Ding.*

A clear chime rang out above the rushing river.

* * *

The welcoming crowd was enormous.

No, it wouldn’t have been the least bit strange to call it massive.

“Waaaaaah!”

“The reinforcements are here! The Murim Alliance reinforcements have arrived!”

Was this what the triumphal processions of the Roman Empire looked like in the textbooks?

The cheers swelled as we drew closer to the walls, then shook the whole city the moment we entered. Everywhere I looked, the streets were packed with dark masses of people.

They filled the broad avenues and narrow alleys, as well as the rooftops of countless buildings—including rows of pavilions—and stretched both arms toward us as they cheered.

The crowd was so enormous that even Cheongpung, who usually loved attention, swallowed nervously and whispered:

“If we stay here much longer, I think my ears might burst, Benefactor.”

“Yeah?”

“Yes. I’m not joking. I’ve never heard anything this loud.”

“Mirror therapy works, all right.”

“Hm? What’s mirror therapy?”

“It’s… never mind. Even if I explained it, Young Hero Cheong wouldn’t change.”

Normally, Cheongpung would have been armed with pure, unbridled curiosity and pressed me to explain what mirror therapy meant. This time, though, he simply continued in a quiet voice.

“There are so many people. Seriously, so many. I stayed in Xining for a while once, but it wasn’t anything like this.”

Cheongpung had spent about a month in Qinghai Province before I had, so the change must have seemed even more striking to him.

Of course, I already had a good idea where this enormous crowd had come from.

*Everyone scattered across Qinghai Province must have gathered in Xining.*

It was only natural.

The same thing had happened earlier in Shanxi, and then in Gansu.

The Great Nation’s imperial court had already declared Dark Heaven rebels and foreign invaders. That was essential to alert the common people, many of whom still thought there was nothing to worry about.

Unlike the Great Faction War, which had barely affected the common folk, Dark Heaven’s actions had long since gone far beyond the bounds of the Murim.

If the Heavenly Demon of the past had set his sights on the Murim, the Lord of Heaven now wanted the whole world.

No—

*Maybe even more than that.*

I forced down the unease that grew sharper with every passing moment and curled my lips into a smile.

So that the countless people surrounding us, covering every direction, might feel a little more at ease when they saw me smile.

“It’s Blazing Flame Divine Dragon Jin Taekyung!”

“Marquis of Shangshan has arrived!”

“Waaaaah! Long live the Great Nation! Long live His Majesty the Emperor!”

There might have been a great many people, but most of them knew little about the affairs of the Murim.

In their eyes, I wasn’t just a young martial artist. I was a divine general, carrying out the Son of Heaven’s solemn imperial command to punish foreign invaders and save them.

At the cheers growing louder by the moment, Cheongpung’s eyes widened.

“Wow. Everyone seems to like you, Benefactor.”

I swallowed a bitter smile and replied in a low voice.

“It looks that way. At least for now.”

“They’ll keep liking you in the future, too. You’re that good a person!”

“A good person…”

I let my voice trail off and looked at the welcoming crowd filling the city.

At a glance, there were hundreds of thousands.

Or perhaps it wouldn’t have been an exaggeration to say there were even more.

At this very moment, all those people were smiling brightly and cheering for me. But I had no way of knowing how long those smiles would stay on their faces.

Or, if the worst really did come to pass, how many of them would survive.

“Young Master Cheongpung.”

“Yes?”

“Yes?”

“Let’s do this. As much as we can.”

I quietly added, still looking at the crowd:

“With our lives on the line.”

Yeah.

Just as we always had.
```
