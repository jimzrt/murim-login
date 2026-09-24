<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0945.txt",
      "sha256": "709c200aecb13f876afa651c69f8326e25586e1830bba55bc762b792a9748a35",
      "bytes": 12461
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ab359693ee3fe459aee9a9a948e13fd24f3a8a93535b42cf4b7122187a204ab3",
      "bytes": 2674
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9fe0f6f78a8493547692832f3f4778c9f0fdc21697955c77a22c8fa8cea623f3",
      "bytes": 233382
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "77bacf38e32aec1081ca7ee788cf1042ca4cd33e654eaef015f754e5dcb3a50c",
      "bytes": 667
    },
    {
      "path": "characters/Jang Il.md",
      "sha256": "85ad8c594b01ce96dea3340adb6f75f56abb9f6c0f6a4c91eaaa6c815403a817",
      "bytes": 477
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "061e921a54c845a4ad20e923025095f9d5688ec57d922f6b6c5e95bff5ccdf5c",
      "bytes": 470
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "50f665ce9493467052aeb556bc5050ee921cb270dcac85988ee59a8e27e1ee40",
      "bytes": 1204
    },
    {
      "path": "characters/Namgung Ryong.md",
      "sha256": "cc5510c92b124095173e905a602b3715996f27742d791a59565cf60c4014c317",
      "bytes": 621
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "fc76244fd0a1365a0678487f3237a11c53c7fc62f21c58de94b83255c82dc9eb",
      "bytes": 1446
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f66daa4bae985fcbafa7ec30ad9fc462f9834c125f917088f6bc22c9afe669f8",
      "bytes": 267309
    }
  ],
  "estimated_tokens": 10304
}
-->

# Durable State Update — Chapter 945

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
1 and safe_through 945. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 945. Profile updates may replace only one
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
  "chapter": 945,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 945,
    "continuity_sources": [945],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "The old bamboo slip Taekyung gave the Divine Physician bears the names Maoshan Sect and White Illusion Jiangshi Art; its full significance is unknown.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao.",
    "War against Dark Heaven is imminent: its main force is targeting Shanxi as a foothold for invasion of the Central Plains, with the Double Ninth Festival as the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The party is traveling toward Shanxi. Namho will contact the Murim Alliance and seek reinforcements from behind; Song Ilseom and Sama Pyo will lead the remaining group toward Shanxi, while Taekyung, Jeok Cheongang, and the Bow Saint advance over a mountain route.",
    "Namgung Ryong has joined Taekyung’s effort against Dark Heaven and is preparing horses, food, and a guide for the journey to Shanxi.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The Bow Saint says the Martial God chose her; she tested Taekyung to confirm he was the chosen one and assess his power and character."
  ],
  "continuity_sources": [
    944,
    943
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?",
    "Where is the Azure Sky Sword King, and who is the figure rising from the shadows?"
  ],
  "safe_through": 944,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 궁성     | **Bow Saint**                 | —              |
| 항산검문   | **Mount Heng Sword Sect**        |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 남궁세가   | **Nangong Family**               |
| 장강수로맹  | **Yangtze River Channel League** |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마적     | **mounted bandits**                              |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 산서     | **Shanxi**             |
| 안휘     | **Anhui**              |
| 항산     | **Mount Heng**         |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 남궁룡 | **Namgung Ryong** | Family Head of the Namgung family. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 남궁룡 | 적천강 | family_head_to_legendary_martial_master | Fire King | formal-deferential | Namgung Ryong accepts three hundred silver nyang as compensation for offending Jeok Cheongang. |
| 적천강 | 남궁룡 | legendary_martial_master_to_family_head | Family Head Nangong | familiar and teasing | Jeok calls him 남궁 가주 while asking whether his son will compete. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 918
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jang Il.md

# Jang Il (장일)

- **Safe through:** Chapter 944
- **Aliases:** None
- **Role:** Jang Il is a junior military officer and one of the seven gate commanders at Yichang’s West Gate.
- **Personality:** He is complacent and greedy, yet regards his restrained corruption as respectable.
- **Voice:** Not established
- **Relationships:** He commands soldiers at Yichang’s West Gate and has an elderly servant.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 880
- **Aliases:** Killing Ghost
- **Role:** A Hubei fisherman who disappeared for a month and returned as the Killing Ghost, a monster that grew stronger and more grotesque with each appearance.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 944
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Namgung Ryong.md

# Namgung Ryong (남궁룡)

- **Safe through:** Chapter 944
- **Aliases:** None
- **Role:** Namgung Ryong is the Family Head of the Nangong Family, which he leads from Anhui, and has committed its support to Jin Taekyung and the Jin Family of Taiyuan against Dark Heaven.
- **Personality:** Authoritative, calculating, decisive, and conscious of the Namgung family’s position as a Murim hegemon.
- **Voice:** Composed, concise, and commanding.
- **Relationships:** Family Head of the Namgung family; commands the Hidden Thread and the Lesser Threads.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 499
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃945화



크르륵. 큭.

이걸 뭐라 불러야 할까.

신음? 아니면 괴성?

그게 무엇이든 한 가지는 확실했다.

지금 이 순간 천천히 몸을 일으켜 세우고 있는 저 장한이, 평범이라는 단어와 한 걸음씩 멀어지고 있다는 것.

“이자는……?”

남궁룡이 의문이 담긴 눈빛으로 장한을 바라보았다.

상대의 정체를 모르니 당연한 반응이다. 그가 도착하기 전, 장한은 우연히 마주친 적천강에게 뭣도 모르고 덤벼들었다가 일권에 기절한 상태였으니까.

“산적입니다.”

“산적?”

“예. 그중에서도 이거죠.”

대답과 함께 머리를 툭 두드리자, 즉각 의미를 알아들은 남궁룡의 고개를 끄덕였다.

“저자가 왜 우두머리 노릇을 하고 있었는지는 잘 알겠군.”

동시에 한층 깊어진 눈빛으로 장한을 응시했다.

“저것이 평범한 산적 우두머리가 보일 수 있는 모습인지는 모르겠지만.”

스아아아.

열기를 머금은 숨결이 주위를 감싸 안는다.

악문 잇새 사이로 수증기와도 같은 입김을 뿜어내는 장한을, 나는 물끄러미 응시했다.

정확히는 지금 막 그의 정수리 위로 떠오른 반투명한 홀로그램 창을.



[Lv.60 장삼]



흔해 빠진 이름에, 척 봐도 산적 같은 얼굴.

하지만 잠깐 사이 그에게 일어난 변화는 극명했다.

허옇게 드러난 흰자위나 계속해서 흘러나오는 뜨거운 입김뿐만이 아니라, 이름 앞에 붙은 숫자가 그것을 증명하고 있었다.

‘레벨이…… 올랐다.’

물론 이러한 레벨 변동이 처음 있는 일은 아니다.

반박귀진(返朴歸眞)의 경지에 올랐거나, 그에 준하는 고수들은 기운을 자유자재로 다룰 수 있기에 [기감]으로도 정확한 레벨을 파악하기 어려우니까.

그러나 눈앞의 산적 두령은 다르다.

저자는 반박귀진의 고수도 아니고, 그렇다고 깨달음을 얻어 레벨이 상승한 경우도 아니었다.

‘더군다나 무려 20레벨씩이나 한 번에 오르는 경우는 없지.’

40레벨에 불과했던 촌구석 산적 두령이 스무 계단이나 껑충 뛰어오른 기현상.

이걸 어떻게 이해해야 하나.

“내 상식으로는 도저히 이해가 안 되는데, 설명 좀 해 보지?”

그리고 물음을 건넨 그 순간.

후웅.

묵직한 파공성과 함께 커다란 주먹이 머리 위를 덮쳤다.

쾅!

단 한 걸음.

옆으로 슬쩍 걸음을 옮기기 무섭게 지면이 푹 꺼지고 풀과 흙이 사방으로 튀었다.

기절하기 전이었다면 결코 보이지 못했을 위력.

나는 어느새 상당한 공력까지 지니게 된 놈을 바라보며 눈매를 좁혔다.

‘이거, 완전히 맛이 갔구만.’

허옇게 드러난 흰자위를 보면서 내심 짐작하긴 했지만, 이 정도면 거의 이성을 상실한 것이나 다름없다.

아니, 어쩌면 기절 상태에서 깨어난 것조차 자의식이 아니었을 수도 있다.

정신이 멀쩡한 놈이라면, 죽고 싶어서 환장하지 않고서야 이 상황에서 내게 덤벼들지는 않을 테니까.

“크아아아아!”

“……이런.”

이쯤 되니 별수 없다.

나는 또다시 맹수처럼 달려드는 놈의 품으로 파고들어, 부드럽게 손을 내뻗었다.

툭.

가슴과 맞닿은 일장(一掌).

그와 동시에 애써 억누르고 또 억누른, 미약한 열기가 손바닥을 타고 뛰쳐나왔다.

퍼엉!

압축된 공기가 터져나가는 소리와 함께, 대포알처럼 튕겨 나간 팔 척의 거구가 공간을 가르며 나무에 처박혔다.

콰아아아앙!

자욱하게 피어오르는 흙먼지 너머, 미동도 없이 널브러진 신형을 한 손으로 붙잡아 질질 끌고 오는 내 모습을 본 산적들의 눈동자가 부릅떠졌다.

“시간 없으니 긴말 안 한다.”

경악과 두려움 속, 나는 나직한 목소리로 말을 이었다.

“아는 거 다 털어놔. 살고 싶으면.”



* * *



남자들은 저마다의 로망을 가슴 한구석에 품은 채 살아간다.

그것이 억 소리가 절로 나는 빨간 스포츠카일 수도 있고, 성공한 사회인의 향기가 물씬 풍기는 서재일 수도 있다.

그리고 그건 나 역시 마찬가지였다.

십 대 시절, 나는 바이크를 향한 로망이 있었다. 여자친구를 뒷자리에 태우고 실컷 밟아 보는 게 꿈이었다.

물론 그때는 알지 못했다.

십 년이 지난 후에도 여자친구가 생기지 않을 거라는 잔인한 사실을.

그리고 잘 빠진 바이크도, 뚜껑 열리는 빨간 스포츠카도 아닌 친환경 사륜구동 준마에 올라탄 채 남자에게 이런 말을 하게 되리라고는.

“허리 좀 꽉 붙잡아. 이 새끼야. 말안장에서 떨어지고 싶어?”

“예, 예!”

“그렇다고 너무 세게 잡지 마라. 살 찝히면 너도 죽는다.”

“히익! 죄송, 죄송합니다!”

두두두두!

거센 말발굽 소리와 울음 섞인 목소리가 뒤섞인다.

남궁룡과 관부에서 이미 손을 써 두었는지, 쉼 없이 말을 몰아 내달리는 우리의 앞을 가로막는 것은 그 무엇도 없었다.

딱 하나 거슬리는 것이라고는, 자꾸만 등 뒤에서 훌쩍이는 사내놈뿐이다.

“그래서, 장퀴네스.”

“……예.”

내게 지게 잃은 나무꾼 행세를 하다가 본업을 들켰던 산적, 장일이 반쯤 포기한 목소리로 대답했다.

십 년이 넘도록 산적 생활을 했다는 장일은 무리 내에서의 위치는 말단에 불과했지만, 그에게는 다른 산적들에게 없는 특이사항이 존재했다.

“십 년 전부터 그놈을 알고 있었다고?”

당연하게도 여기서 말하는 ‘그놈’이란, 지금쯤 남궁세가로 끌려가고 있을 산적 두목이었다.

“예. 소인이 이 바닥에 처음 발을 디뎠을 때부터 알고 지냈습니다요. 한때는 피를 나눈 형제나 다름없었지요.”

“산적 주제에 형제는 니미. 아주 지랄 염병을 떠는구먼.”

나란히 달리는 와중에도 귀를 기울이고 있던 적천강의 소신 발언에, 미간을 좁힌 궁성이 작게 혀를 찼다.

“괜히 끼어들지 말고, 마저 얘기하게 두죠.”

“왜? 이젠 혼잣말도 못 하나?”

“당신은 정말 여전하군요. 머리털만 사라졌지, 그때와 별반 다를 것이 없…….”

“지금 말 다 했나?”

적천강의 눈빛이 착 가라앉았다. 최근 들어 봄철 새싹처럼 슬금슬금 고개를 내미는 머리카락을 애정 어린 손길로 가꾸고 있던 그는 분노를 숨기지 않았다.

“두 분은 그만하시고. 넌 계속 얘기해.”

초절정 고수 두 명이 차가운 눈빛을 주고받는 와중에도 말은 계속해서 달린다. 마른침을 꿀꺽 삼킨 장일이 입을 열었다.

“하, 하여튼 그때부터 지금까지 줄곧 두령을 따라다녔습니다. 안휘성으로 산채를 옮긴다고 하자 모두가 미쳤다며 떠날 때에도, 소인은 믿음과 의리 하나만으로 따라왔습죠.”

“안휘성으로 산채를 옮겼다고?”

“예에. 원래는 호북(湖北) 인근이었는데, 두령이 어느 날 갑자기 그렇게 결정해 버렸지 뭡니까. 다들 반발이 극심했지요.”

그때가 떠오르는 듯, 입맛을 다신 장일이 말을 이었다.

“사실 소인도 말은 안 했지만, 더 늦기 전에 이 바닥 생활 접고 떠날 생각까지 했습니다요.”

“어째서? 산채를 옮기는 게 그 정도로 큰일인가?”

“어휴, 모르시는 말씀을. 짐 싸 들고 가는 거야 잠깐의 수고로움이니 그렇다 쳐도, 안휘에는 남궁세가가 있지 않습니까.”

나는 미간을 좁혔다. 언뜻 듣기에도 장일의 말이 영 이치에 맞지 않았기 때문이었다.

“그건 이유가 못 되지. 원래 자리 잡고 있던 호북에도 무당파와 제갈세가가 있었을 텐데.”

장일이 단번에 고개를 내저었다.

“명문 대파가 몇 개나 있느냐가 중요한 게 아닙니다. 인근에 어떤 명문 대파가 있느냐를 봐야지요.”

“아.”

“무당파나 제갈세가는 비교적 온건한 편이라, 어지간해서는 피를 보지 않고 마무리 짓습니다. 하지만 남궁세가는…….”

문득 말꼬리를 흐린 장일이 부르르 몸을 떨었다.

“그래서인지 안휘성의 무림인들도 인정사정 봐주는 법이 없습니다. 일이 틀어지면 목 날아가는 것도 각오해야지요.”

우습다 못해 기가 찬 일이다.

산적 주제에 그런 것까지 일일이 따져 가며 일을 하다니.

하지만 그것과는 별개로, 두령의 선택은 확실히 이상한 구석이 있었다.

남궁세가로도 모자라 황도가 인접한 절강과 안휘의 경계선에 산채를 차렸으니까.

“그렇게 산채를 옮긴 시점이 언제지?”

“아마…… 석 달? 그쯤 된 것 같습니다.”

“그럼 함께 있던 산적들은? 이야기를 들어 보니 전에 있던 놈들은 다 도망간 것 같은데.”

“송충이는 솔잎만 먹어야 한다더니, 막상 와 보니 녹림맹 소속도 아닌 주제에 안휘성에서 산적질을 하는 간 큰 놈들이 있지 뭡니까.”

“그래서, 그놈들을 새롭게 휘하로 들였다?”

“그렇지요. 어느 날 저만 남겨 두고 홀로 떠나더니, 작은 규모의 산채 두 개를 흡수해서 돌아왔습니다.”

장일이 서글프게 덧붙였다.

“덕분에 여기 와서도 말단 노릇이나 하고 있지요.”

나이 든 중늙은이의 신세 한탄에는 조금도 관심 없다. 나는 머리카락을 스치는 바람을 느끼며 내심 중얼거렸다.

‘아무리 규모가 작다지만 산채 두 개를, 그것도 단신으로?’

당연히 개소리다.

레벨이 오르기 전에 봤던 놈의 모습은, 어떻게 쌓았는지 모를 콩알만 한 공력과 타고난 용력(勇力)만 믿고 날뛰는 어중간한 이류에 지나지 않았으니까.

‘잘 쳐줘야 일류 문턱. 그 정도로는 턱도 없지.’

수십 명이나 되는 다수를 상대로 승산을 논할 수 있는 것은 초일류 어림부터다.

그것도 적들의 수준이 최소 한 수 이상 뒤떨어진다는 전제하에.

“역시, 믿는 구석이 있었구만.”

“예?”

“네가 두령으로 섬기는 그놈. 분명 그렇게 강한 놈은 아니었을 텐데? 갑자기 무슨 자신감으로 안휘성으로 옮기고, 두 개나 되는 산채를 규합했지?”

“그건…….”

잠시 머뭇거리던 장일이 고개를 끄덕였다.

“저도 내심 희한하긴 했습니다. 소인의 기준에서야 강하지만, 두령의 무공이 딱히 강한 것은 아니어서…….”

천하 어느 곳이든, 일대에서 두각을 드러낸 산적은 결국 둘 중 하나를 선택해야 한다.

제법 뛰어난 무공을 믿고 깝치다가 명문 대파의 제자들에게 토벌당하거나, 녹림맹(綠林盟)에 소속되거나.

‘수적의 경우에는 장강수로맹이고.’

자고로 대기업 이기는 골목상권은 없는 법이다.

녹림맹의 인증을 받은 공식 가맹점주가 되면 상당한 세금을 바쳐야겠지만, 대놓고 패악질을 벌이지 않는 이상은 명문 대파의 토벌은 피할 수 있다.

단순한 도적놈에서, 최소한의 선은 지키는 공생(共生)으로 거듭나는 것이다.

‘하지만 그놈은 어디에도 해당하지 않았지.’

지난 십 년 동안 두각을 드러내지 못한 놈이, 황도가 위치한 절강성과 엎어지면 코 닿을 거리에 산채를 차렸다.

아무리 중양절이라는 대목을 노리고 한탕을 취하려 한다 해도 이건 상식적으로 설명이 안 된다.

갑자기 훌쩍 강해진 그 모습처럼.

‘이건 기연(奇緣)이라도 부를 수도 없어.’

그리고 이러한 일련의 상황들은, 나로 하여금 이미 일 년도 넘게 지난 옛 기억을 떠올리게 만들었다.

‘풍양. 적풍단주 풍양.’

항산검문을, 아니 산서성을 노렸던 마적단의 두목.

그리고 놈에게 그 거대한 야망을 안겨 주었던 한 가지 물건.

‘잠력단……!’
```

## Final English reading copy

```markdown
# Chapter 945

Grrk. Krrk.

What should I call that?

A groan? Or a roar?

Whatever it was, one thing was certain.

That burly man slowly rising to his feet right now was moving one step farther away from the word *ordinary*.

“Who is that…?”

Namgung Ryong looked at the man with a questioning gaze.

It was only natural that he didn’t know who the man was. Before Namgung Ryong arrived, the burly man had run into Jeok Cheongang by chance, picked a fight without knowing any better, and been knocked unconscious with a single punch.

“He’s a bandit.”

“A bandit?”

“Yes. And he’s the head of the bunch.”

I tapped the top of my head, and Namgung Ryong nodded as he immediately understood what I meant.

“I can see why that man was acting like their leader.”

His gaze fixed on the burly man, growing even more intent.

“Though I don’t know if an ordinary bandit chief could look like that.”

Ssshhh.

A breath carrying heat enveloped the area.

I watched the burly man as he exhaled vaporous breaths through his clenched teeth.

More precisely, I was staring at the translucent holographic window that had just appeared above his head.

> **System**
> Lv. 60 Jang Sam

A painfully common name. A face that looked like a bandit at a glance.

But the change that had come over him in such a short time was unmistakable.

It wasn’t just the whites of his eyes showing or the hot breath spilling from his mouth. The number before his name proved it.

*His Level… went up.*

Of course, this wasn’t the first time I’d seen someone’s Level change.

Masters who had reached the realm of Returning to Simplicity, or something close to it, could control their energy freely. Even Qi Sense couldn’t accurately read their Level.

But this bandit chief was different.

He wasn’t a master of Returning to Simplicity, nor had he gained enlightenment and raised his Level that way.

*And people don’t jump twenty Levels all at once.*

A bizarre phenomenon: a backwater bandit chief who’d been only Level 40 suddenly leaping up twenty steps.

How was I supposed to make sense of that?

“I can’t understand this at all, based on what I know. Care to explain?”

The moment I asked—

Whoosh.

A huge fist came down over my head with a heavy whistle.

Crash!

Just one step.

I’d barely shifted to the side when the ground caved in, sending grass and dirt flying in every direction.

That was power he could never have shown before he passed out.

I narrowed my eyes as I looked at the man, who now had a considerable amount of internal energy.

*He’s completely lost it.*

I’d suspected as much from the whites of his eyes, but at this point, he’d practically lost his reason.

No—maybe even waking up from his unconscious state hadn’t been his own doing.

A man in his right mind wouldn’t charge at me in this situation unless he had a death wish.

“Raaaagh!”

“…Well, then.”

There was no helping it now.

As he charged at me like a wild beast again, I slipped into his reach and gently extended my hand.

Tap.

My palm touched his chest.

At the same time, a faint heat—one I’d worked hard to suppress, over and over—burst out through my palm.

Boom!

With a sound like compressed air exploding, his eight-foot frame shot away like a cannonball, cutting through the air before slamming into a tree.

Kraaaash!

Beyond the thick cloud of dust, I grabbed his motionless body with one hand and dragged him back. The bandits’ eyes widened.

“We’re short on time, so I’ll keep this brief.”

As they stared in shock and fear, I continued in a low voice.

“Tell me everything you know. If you want to live.”

* * *

Every man lives with some dream tucked away in a corner of his heart.

It might be a red sports car that costs a fortune, or a study that practically reeks of a successful professional’s life.

I was no different.

When I was a teenager, I dreamed of having a motorcycle. I wanted to take my girlfriend for a ride on the back and really open it up.

Of course, I didn’t know then.

That even ten years later, I’d still have no girlfriend.

And that instead of straddling a sleek motorcycle or a red convertible, I’d be riding a green, four-wheel-drive thoroughbred and saying this to a man:

“Hold my waist tight, you bastard. You want to fall off the saddle?”

“Y-Yes!”

“But don’t grab too hard. If you pinch me, you’ll die.”

“Eek! I’m sorry, I’m sorry!”

Thud-thud-thud!

The thunder of hooves mingled with a tearful voice.

Maybe Namgung Ryong and the authorities had already made arrangements, because nothing got in the way of us as we rode nonstop at full speed.

There was only one thing bothering me: the guy behind me kept sniffling.

“So, Jangquines.”

“…Yes.”

Jang Il answered in a voice that sounded half resigned. He was the bandit who’d posed as a woodcutter who’d lost his carrying frame, only for me to catch him at his real trade.

Jang Il had been a bandit for more than ten years. He was at the very bottom of the pecking order, but there was one unusual thing about him that the other bandits didn’t share.

“You’ve known that guy for ten years?”

“Y-Yes. I’ve known him ever since I first set foot in this line of work. At one time, we were like brothers who’d shared blood.”

“Brothers, my ass. You’re a bandit. What a load of bullshit.”

Jeok Cheongang, who’d been listening as he rode beside us, gave his candid opinion. The Bow Saint frowned and clicked her tongue softly.

“Why don’t you stay out of it and let him finish?”

“What? Am I not allowed to talk to myself anymore?”

“You really haven’t changed. You’ve lost all your hair, but otherwise you’re just like you were back then…”

“Do you have something to say?”

Jeok Cheongang’s gaze turned icy. Lately, his hair had been slowly sprouting like spring shoots, and he’d been tending to it with loving care. He made no attempt to hide his anger.

“That’s enough, you two. You, keep talking.”

Even as the two Supreme Peak masters exchanged cold looks, the horses kept running. Jang Il swallowed hard and continued.

“A-Anyway, I followed the chief from then until now. When he said we were moving the stronghold to Anhui Province, everyone called him crazy and left, but I followed him on nothing but faith and loyalty.”

“You moved the stronghold to Anhui Province?”

“Yes. It was near Hubei originally, but one day the chief suddenly decided that was what we were doing. Everyone was dead set against it.”

Jang Il smacked his lips, as if remembering the day, then went on.

“Truth be told, I didn’t say anything, but I was even thinking about quitting this life and leaving before it was too late.”

“Why? Was moving the stronghold that big a deal?”

“Oh, you don’t know what you’re talking about. Packing up and leaving would’ve been a bit of a hassle, sure, but Anhui has the Nangong Family.”

I frowned. Even at a glance, what Jang Il was saying didn’t quite make sense.

“That’s not a reason. Wudang and the Zhuge Clan were in Hubei, where you were before.”

Jang Il immediately shook his head.

“It’s not about how many great sects there are. You have to look at which great sects are nearby.”

“Oh.”

“Wudang and the Zhuge Clan are relatively mild. Most of the time, they settle things without bloodshed. But the Nangong Family…”

Jang Il trailed off, then shuddered.

“Maybe that’s why the martial artists of Anhui don’t go easy on anyone, either. If things go wrong, you have to be ready to lose your head.”

It was ridiculous—so ridiculous I could hardly believe it.

They were bandits, and they still took things like that into account when deciding where to operate.

But separately from that, there was definitely something strange about the chief’s choice.

He’d built a stronghold right on the border between Zhejiang and Anhui, with the imperial capital close by—and the Nangong Family nearby, too.

“When did you move the stronghold?”

“Probably… three months ago? Around then.”

“What about the other bandits who were with you? From what you’ve said, it sounds like all the ones from your old place ran off.”

“They say you should stick to your own turf, but when we got here, we found these gutsy bastards playing bandit in Anhui without even belonging to the Green Forest Alliance.”

“So your chief brought them under his command?”

“That’s right. One day, he left on his own, leaving only me behind. Then he came back after taking over two small strongholds.”

Jang Il added sadly,

“And here I am, still at the bottom of the pecking order.”

I had no interest in listening to an old man complain about his lot in life. Feeling the wind brush past my hair, I thought to myself,

*Even if they were small, he took over two strongholds all by himself?*

Of course that was bullshit.

Before his Level went up, the man had been no more than a middling Second Rate fighter, relying on some tiny amount of internal energy—who knew how he’d built it up—and his natural strength.

*At best, he was on the threshold of First Rate. That wouldn’t come close.*

You had to be at least Supreme First Rate to even talk about having a chance against dozens of people at once.

And that was assuming your opponents were at least a full level below you.

“So he had something to fall back on after all.”

“Pardon?”

“The man you followed as chief. He wasn’t that strong, was he? What gave him the confidence to move to Anhui and unite two whole strongholds?”

“Well…”

Jang Il hesitated for a moment, then nodded.

“I did find it strange myself. By my standards he was strong, but his martial arts weren’t anything special…”

Anywhere under Heaven, a bandit who stood out in his region eventually had to choose one of two paths.

Either trust in his decent martial arts and swagger around until disciples of a great sect came to wipe him out, or join the Green Forest Alliance.

*In the case of river bandits, there was the Yangtze River Channel League.*

A small business never beats a corporation.

Once you became an officially recognized franchisee of the Green Forest Alliance, you had to pay substantial taxes, but as long as you didn’t openly commit atrocities, you could avoid being hunted down by the great sects.

You went from being a mere bandit to part of a symbiotic system that at least followed a few basic rules.

*But that man fit neither category.*

For the past ten years, he’d never made a name for himself. Then he built a stronghold right next to Zhejiang Province, where the imperial capital stood.

Even if he was trying to cash in on the Double Ninth Festival holiday, there was no way to explain it logically.

Just like the way he’d suddenly grown so much stronger.

*You couldn’t even call this a fortuitous encounter.*

And this whole string of strange events brought back a memory from more than a year ago.

*Pung Yang. Pung Yang, the Red Wind Band Leader.*

The chief of the mounted bandits who’d set his sights on the Mount Heng Sword Sect—no, on Shanxi Province.

And the one item that had given him such grand ambitions.

*The Temporary Strength Pill…!*
```
