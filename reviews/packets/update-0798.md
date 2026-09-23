<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0798.txt",
      "sha256": "9e252ad54b787d3895a0038d6e9f1c4c88968f557602f62910c97752c3181c75",
      "bytes": 12985
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6642ab699739d3453d420aa3edea507be275fa5f7b977928a7cf486e67c3352e",
      "bytes": 1426
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "97c6dd5161ec61a3fa52be729a8ce6bbdcdcabe92ff1394a89858fdd6b8da351",
      "bytes": 224372
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a32dffbccae72f42b116663cd50266ec2ce51b52930953b471897fbe8633fb8e",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "6f9540aab4742421b61433f98377ea01000f8046ec9c17671844f2aa62bb2ad7",
      "bytes": 682
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4f86d20a9e57e938a0410b60eadede2c903fb5fb847a292ec20c96a063ec8b17",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e425ba2ea20a710ce5892a21f92d5796495b2636031410999942da23183daef7",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "fe50f5f787ed99c026a114cb01277e1140d8578d4b7083396271a32ad5efceb1",
      "bytes": 666
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "2075572a5e0babce68ae365ed4937b162a9fefec2c4dd548f27cab441e5a137b",
      "bytes": 728
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "904f8e2202fbca2ddec9949e1a3e400fc5b1d6514473b0e5c88e023e83f3bd3d",
      "bytes": 492
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a0c96e30d11ab7a2dbfa66db966db299ed0a18441394d9a45bce2e4b5d500a6",
      "bytes": 246412
    }
  ],
  "estimated_tokens": 9982
}
-->

# Durable State Update — Chapter 798

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 798. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 798. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 798,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 798,
    "continuity_sources": [798],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing the Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet leads the revived Hasasin and is an exceptionally powerful combatant; he has attacked J1 during the search-team withdrawal.",
    "Yamamoto Genji is alive at the scene of The Prophet’s attack on J1, with reinforcements arriving.",
    "Search teams are withdrawing from the region; more than 70 percent have returned, while some remain in transit or temporarily out of contact.",
    "The Skeleton King’s undead force is moving among the search teams; headquarters has requested his support at J1."
  ],
  "continuity_sources": [
    796,
    797
  ],
  "open_questions": [
    "Who is the current Prophet, and where is he?",
    "What caused the deaths of Siegfried Wassmann and the twenty people found in the desert?",
    "What disappeared from the desert without a trace, as described by the Skeleton King?",
    "What components does The Prophet still need, and what is he preparing?",
    "Will Yamamoto Genji survive The Prophet’s attack, and who else from J1 survived?"
  ],
  "safe_through": 797,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 질풍불참 as “Swift No-Show” in the Genji/Switch Strike joke."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 답설무흔 | **Treading Snow Without a Trace** | Comparable movement feat that leaves no footprints on snow. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 힐러 | invading Hunter to Ares healers | you people | profane and contemptuous | Uses 당신들이 while demanding that the healers save their fallen comrades and question Go Jun's order. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 796
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 797
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild operative and elite fixer personally selected and trained by Michael, now held captive by Jin Taekyung.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 796
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 796
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 796
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 797
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is the mysterious, exceptionally powerful leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 797
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and the sole known survivor at the scene of The Prophet’s attack on J1 as reinforcements arrive.
- **Personality:** Prideful and easily offended, he is prone to self-aggrandizement and paranoid, self-serving assumptions.
- **Voice:** Not established.
- **Relationships:** Not established.

## Korean source

```text
＃798화



나도 안다. 아무리 뛰어난 능력이 있어도 이 세상에서 벌어지는 모든 불행을 막을 수는 없다는 것을.

하지만 그럼에도 일 초가 한 시간처럼 느껴지는 이유는, 지금 이 순간에도 피를 흩뿌리며 쓰러지고 있을 저들의 불행이 나로부터 비롯되었기 때문이다.

그들을 머나먼 이국의 사막으로 부른 것도, 죽음으로 몰아넣은 것도 나다.

맹주(盟主)라는 이름표를 단 이상, 나는 이 전쟁이 끝날 때까지 괴로워해야 한다.

누구보다 앞장서고 치열하게 싸워야 하는 숙명을 부여받았다.

쐐애애액!

나는 세찬 바람을 가르며 쏘아졌다.

이미 오래전 답설무흔(踏雪無痕)의 경지를 넘어선 경공은 고운 모래 위에도 흔적을 남기지 않았고, 한 걸음을 나아갈 때마다 수십여 미터의 거리가 지워졌다.

‘더, 더, 조금이라도 더 빨리.’

단 한시도 뒤를 돌아보지 않았지만, 사막 위의 요새처럼 우뚝 서 있던 본부가 보이지 않을 만큼 멀리 왔다는 것쯤은 알 수 있었다.

하늘 위로 솟구치며 확인했던 흐릿한 불빛에 점점 가까워지고 있다는 사실도 함께.

‘그런데 왜…….’

왜 이리도 조용한 걸까.

차마 이어 갈 수 없던 그 생각에 가슴이 쿵, 하고 내려앉는다. 이를 악문 나는 온 힘을 실어 진각(震脚)을 밟았다.

구구궁.

발끝을 타고 흘러간 공력이 지면을 뒤흔들고, 순간 용수철처럼 한껏 수축했던 근육이 반동과 함께 폭발적인 힘을 뿜어냈다.

퍼엉!

묵직한 파공성과 함께 포탄처럼 쏘아지는 신형. 그와 동시에 바람을 타고 귓가로 전해지는 희미한 소음들.

- ……도대체……놈이.

- 한스! 한스!

- 도주…… 본부에 생존자…… 연락.

드문드문 끊기는 사람들의 목소리와 차량의 엔진음.

빠르게 가까워지며 느껴지는 인기척도, 들려오는 소음도 많다. 다행히도 피해가 그리 크지 않음이 분명했다.

“아.”

그제야 안도 섞인 탄식을 흘린 나는 더욱더 속도를 높였다.

그리고 잠시 후, 눈 앞에 펼쳐진 광경을 본 순간 깨달았다.

앞서 느꼈던 모든 인기척과 소음들은, 이미 나보다 한발 앞서 이곳에 도착한 이들의 것이었다는 사실을.

“……!”

나는 석상처럼 굳은 채 미라처럼 바짝 말라붙은 수백여 구의 시체를 바라보았다.

이쪽을 향한 사람들의 시선도, 웅성거림도 메아리처럼 멀게만 느껴진다.

오직 한 단어만이 머릿속을 점령했다.

‘선지자.’

틀림없다.

바로 이곳에, 그놈이 있었다.

그리고 어쩌면…….

‘아직 근처에 있다. 분명히.’

죽은 이들에 대한 추모는 미루어야 한다.

오늘 이 자리에서 놈을 잡지 못한다면 몇십 배, 몇백 배나 되는 희생을 치러야 할 테니까.

‘어디냐.’

끓어오르는 가슴과 달리 머릿속은 얼음장처럼 차갑다. 나는 그 어느 때보다 곤두선 감각을 느끼며 기감(氣感)을 펼쳤다.

솨아아악.

보이지 않는 기운이 모래 위를 타고 뻗어 나감과 동시에, 신형을 힘차게 내쏘았다.

콰아아아!

파도처럼 솟구친 모래알 너머로 언뜻 익숙한 얼굴이 스쳐 지나간다.

지원군이 분명한 사람들 사이로 다급한 표정을 한 스켈레톤 킹이 뭐라 외치고 있었지만, 이미 빛살처럼 사막을 가로지르는 내 모든 감각은 오롯이 한 존재만을 좇고 있었다.

선지자.

병든 나무의 마지막 뿌리를, 오늘 이곳에서 뽑아내야 한다.



* * *



세상 모든 일이 바라는 대로 풀렸다면, 아마도 나는 지금 이곳에 없었을 것이다. 아버지가 돌아가실 일도 없었을 테고, 어머니가 아프지도 않았겠지.

만약 그랬다면 나는…… 모르겠다.

내신은 개판이고 장점이라고는 몸 튼튼한 것밖에 없었으니까.

그래, 시발.

어차피 결국 이루어지지 않을 헛된 바람이고 개소리다.

세상일은 언제나 내가 원하는 대로 흘러가지 않았고, 그건 이번에도 역시 마찬가지였다.

“끔찍한 아침이군. 안 그래, 진?”

나는 지친 얼굴로 인사를 건네는 매직 존슨 옆에 털썩 주저앉았다.

우리는 서로에게 결과를 묻지 않았지만, 이미 여섯 시간에 걸친 수색이 수포로 돌아갔다는 것을 알고 있었다.

그럼에도 굳이 입을 여는 이유는, 혹시나 하는 기대 때문이다.

“존슨.”

“미안해.”

“…….”

“인근 700km를 샅샅이 뒤졌어. 시리아와 이라크를 반쯤 협박하다시피 해서 협조까지 얻어냈다고. 그런데, 제기랄.”

선지자는 사라졌다.

아니, 증발했다.

마치 원래부터 이 세상에 존재하지 않았던 것처럼.

내 뒤를 이어 곧장 수색에 참여했던 정예 헌터들이 모두 귀신에 홀린 듯한 표정을 짓고 있는 것도 당연한 일이었다.

“분명히 간발의 차였는데, 도대체 어디로 도주한 거지?”

지원군의 움직임은 신속했다.

총원 이백여 명의 일본 헌터들로 구성된 J1팀이 교전 발생을 알린 지 불과 15분도 되지 않아 현장에 도착했으니까.

문제는 지원군이 도착하기 직전 전장을 이탈한 선지자를 어디에서도 찾을 수 없다는 것이었다.

“진. 적어도 내가 아는 한에서, 이건 한 가지로밖에 설명이 안 돼.”

매직 존슨과 시선이 마주친 내가 조용히 뇌까렸다.

“마법.”

“그래. 선지자는 마법사야. 그것도 대마도사라 불러도 부족함이 없을 정도로 뛰어난 수준의 마법사.”

매직 존슨의 마법으로도, 스켈레톤 킹의 언데드 군단으로도, 마지막으로 나조차도 놈의 흔적을 찾지 못했다.

그렇다면 남은 건 하나뿐이다.

마법.

이해할 수 없는 현상을 접했을 때, 사람들은 기적 혹은 마법 같은 일이라 표현하고는 한다.

선지자의 경우에는 후자가 틀림없다.

놈이 종교에 세뇌당한 광신도들이 믿는 것처럼 정말 신의 선택을 받은 인물일 리는 없으니까.

‘마법사라.’

문득 후긴이 했던 말이 떠올랐다.

원거리형 헌터로 보였다는 그 진술.

반신반의했지만 이번만큼은 무게추가 그쪽으로 쏠릴 수밖에 없었다.

선지자는 마법사일 가능성이 높다. 그것도 매직 존슨의 눈을 피해 종적을 감출 수 있을 만큼 뛰어난 경지의 마법사.

혹은…….

‘수하 중에 그 정도 수준의 마법사가 있거나.’

만약 그게 사실이라면 최악 중의 최악이겠지만, 다행히도 내 생각을 들은 매직 존슨은 대번에 고개를 저어 보였다.

“그건 아냐.”

“저도 그러길 바라지만, 혹시 모를 가능성은…….”

“선지자는 분명히 혼자였어.”

“네?”

매직 존슨의 어조에서 묻어 나오는 것은 단순한 짐작을 넘어선 확신이었고, 반사적으로 되물은 나는 곧이어 들려온 한 마디에 그 이유를 알 수 있었다.

“생존자가 있어, 진.”

“……!”

“J1팀의 유일한 생존자. 네가 도착하기 얼마 전에 깨어났어.”

유일한 생존자.

그 단어에 더 이상 듣고만 있을 수만은 없었다. 자리에서 벌떡 일어난 나는 매직 존슨에게 물었다.

“그 친구, 지금 어디에 있습니까?”



* * *



생존자는 각종 의료 장치를 주렁주렁 매단 채 누워 있었다.

침대 옆에서 심각한 얼굴로 대화를 나누고 있던 최 팀장과 스켈레톤 킹은 나를 발견하고 뭐라 말할 것처럼 입을 열었지만, 이내 굳게 다물었다.

아침이 밝도록 이어진 수색이 헛수고로 돌아갔다는 것쯤은, 내 표정만 봐도 알 수 있었을 것이다.

“저 사람이야?”

내 질문의 의미를 즉각 알아들은 스켈레톤 킹이 고개를 끄덕였다.

“그래. 그곳에 있던 인간 중 유일한 생존자다.”

“그럼 내가 현장에 막 도착했을 때는…….”

“그때는 이미 부상자 한 명 없이 모두 숨이 끊긴 후였어. 저 인간도 심각한 상태였지만 운이 좋았지. 네놈은 오자마자 제대로 듣지도 않고 곧장 떠나 버렸고.”

그제야 급박했던 당시 상황이 머릿속에서 되살아났다.

처음 현장으로 향하던 그때 사람들의 목소리 사이로 섞여 들려온 생존이라는 단어와, 떠나려는 내게 뭐라 말하려던 스켈레톤 킹의 모습도.

“말하기도 전에 가 버리더군. 이 몸도 바로 쫓아가려다가 말았다. 나까지 자리를 비운 상황에서 또다시 무슨 일이 생길 수도 있으니까.”

스켈레톤 킹의 판단이 옳았다. 어쩌면 나보다도 냉철하게 상황을 읽었을지도 모른다.

말없이 입술을 깨무는 내 모습에 최 팀장이 입을 열었다.

“두 분 다 맞는 판단을 하셨습니다. 지금 우리에게 중요한 건 생존자가 있다는 점이고요.”

기백이 넘는 인명 피해는 안타깝지만, 생존자가 있다는 것은 천운이다.

그 참혹한 현장에서 살아남은 그에게도. 그리고 우리 모두에게도.

“조금 전, 그러니까 발견 직후 여섯 시간 만에 깨어났습니다. 담당 힐러 말에 의하면 포션을 충분히 복용하고 마지막 회복 단계에 접어들었으니 문제없을 거라더군요.”

나는 멍하니 입을 벌린 채 허공만 바라보고 있는 생존자를 유심히 살폈다.

그리 안 괜찮아 보이는 건 둘째치고, 어딘지 모르게 익숙한 얼굴이다.

거기에 더해서 굳이 맥을 짚어 보지 않아도 자연스럽게 느껴지는 몸속 충만한 기운까지.

‘잠깐. 이 사람 설마?’

뭔가를 깨닫고 고개를 돌리자, 최 팀장이 내 생각을 읽은 것처럼 고개를 끄덕였다.

내 귓가에만 전달되는 나지막한 전음(傳音)과 함께.

- 진태경 씨께서 생각하시는 그 사람이 맞습니다. 일본의 S급 헌터, 야마모토 겐지가 J1팀의 유일한 생존자입니다.

- ……!

- 간발의 차였습니다. 대략적인 상황을 유추해 보니 지원 병력이 도착하기 직전이라, 선지자로서도 발목이 잡힐 것을 우려하여 확실하게 끝을 맺지 못한 것 같더군요.

지원 병력으로 현장에 출동했던 오백 명의 헌터들은 운이 좋았다.

선지자가 조금만 더 멍청했더라면, 혹은 스스로의 힘을 과신했더라면 그들 역시 죽음을 면치 못했을 테니까.

그러나 선지자는 영리하면서도 신중했고, 한 자리에서 시간을 지체할수록 더욱 큰 위협에 직면하리라는 것을 알고 있었다.

그건 인류에게는 불행이지만, 살아남은 이들에게는 행운이다.

그런 의미에서 초점이 흐려진 눈동자로 줄곧 허공만 바라보는 눈앞의 생존자, 아니 야마모토 겐지는 그중에서도 천운(天運)을 타고난 셈이다.

물론 비슷한 경험을 겪은 나는 그렇게 생각하지 않았지만.

‘빌어먹을.’

나는 야마모토 겐지가 싫다.

그를 향한 감정을 정의하자면 싫은 것을 넘어 혐오에 가깝다.

많은 이들이 레비아탄을 저지하기 위해서 목숨을 걸고 싸우던 그때, 말 같지도 않은 핑계를 대며 느지막이 나타났으니까.

내가 굳이 그런 부류의 인간을 세계 헌터 연맹에 집어넣게 된 이유는 단순히 놈이 S급 헌터여서였다.

아무리 병신이어도 한 번쯤은 제 몫을 해낼 병신이라는 믿음 때문에.

하지만 내가 지금까지 놈을 어떻게 생각해 왔건 간에, 나는 야마모토 겐지를 욕할 자격이 없다.

모두가 죽었는데 왜 혼자 살아 돌아왔느냐며 물을 생각도 없다.

내가 바로 놈을, 그들을 사지(死地)로 보낸 장본인이니까.

턱.

나는 야마모토 겐지의 손목을 잡고 공력을 흘려보냈다.

따스한 온기를 머금은 열양지기가 완맥을 타고 몸속으로 흘러 들어가자, 불규칙하던 맥박이 안정되고 창백한 얼굴 위로 불그스름한 열기가 감돌았다.

“야마모토.”

나직하게 이름을 부르자, 그가 반응했다. 바싹 메마른 입술이 달싹인다.

“……아, 아아.”

나는 말하는 법을 잊은 사람처럼 입만 벙긋거리는 그를 가만히 지켜보며 계속해서 공력을 흘려보냈다.

그렇게 얼마나 시간이 흘렀을까. 간신히 초점이 돌아온 눈동자로 나를 바라본 야마모토 겐지가 마침내 입을 열었다.

“조…….”

“조?”

“조센징?”

아니, 이 씨발 새끼가.
```

## Final English reading copy

```markdown
# Chapter 798

I knew. No matter how extraordinary your abilities were, you couldn’t prevent every tragedy in the world.

And yet every second felt like an hour because the people who were collapsing in pools of blood at this very moment were suffering because of me.

I was the one who’d called them to this distant desert in a foreign land. I was the one who’d led them to their deaths.

The moment I took on the title of Alliance Leader, I was bound to suffer until this war was over.

I’d been given the fate of fighting harder and leading from the front more than anyone else.

*Whoosh!*

I shot forward, cutting through the fierce wind.

My lightness skill had long since surpassed the realm of Treading Snow Without a Trace. It left no footprints even on fine sand, and each step erased dozens of meters.

*Faster. Faster. Just a little faster.*

I hadn’t looked back for even a second, but I knew I’d come so far that the headquarters, which had stood like a fortress in the desert, was no longer visible.

I was also getting closer and closer to the faint lights I’d spotted when I’d leapt into the sky.

*But why…?*

Why was it so quiet?

At the thought I couldn’t bring myself to finish, my heart sank. I gritted my teeth and stamped down with all my strength.

*Rumble.*

The internal energy flowing through my toes shook the ground. For an instant, my muscles had compressed like a spring; now they recoiled, unleashing explosive force.

*Boom!*

My body shot forward like a cannonball with a heavy boom of displaced air. At the same time, faint sounds reached my ears on the wind.

—…What the hell… that bastard…

—Hans! Hans!

—Fled… survivor… contact headquarters…

The broken-off voices of people, scattered among the sound of vehicle engines.

There were plenty of people nearby, and I could hear plenty of noise as I drew closer. The damage clearly wasn’t too severe.

“Ah.”

Only then did I let out a sigh of relief and pick up the pace.

A moment later, the instant I saw the scene spread out before me, I understood.

All the signs of life and noise I’d sensed earlier belonged to people who had already arrived here ahead of me.

“……!”

I froze like a statue, staring at hundreds of bodies, dried out as tightly as mummies.

The people’s eyes turned toward me. Their murmuring felt as distant as an echo.

Only one word filled my mind.

*The Prophet.*

No doubt about it.

He’d been here.

And maybe…

*He’s still nearby. He has to be.*

I’d have to put off mourning the dead.

If we didn’t catch him here today, we’d have to pay a price tens, even hundreds of times greater.

*Where are you?*

My heart was boiling, but my mind was as cold as ice. My senses were sharper than ever as I spread my Qi Sense.

*Fwoosh.*

As invisible energy swept across the sand, I launched myself forward.

*Whooosh!*

Beyond the sand surging up like a wave, a familiar face flashed into view.

Amid the people who were clearly reinforcements, the Skeleton King was shouting something with an urgent expression. But already, as I streaked across the desert like a beam of light, every one of my senses was fixed on a single presence.

The Prophet.

Today, right here, I had to pull out the last root of a diseased tree.

* * *

If everything in the world had gone the way I wanted, I probably wouldn’t be here now. My father wouldn’t have died, and my mother wouldn’t have gotten sick.

If that had happened, I… I don’t know.

My school grades were a complete disaster, and my only strong point was that I was healthy.

Yeah, fuck.

It was all just a pointless wish and a load of bullshit, something that was never going to happen anyway.

Things in this world had never gone the way I wanted. This time was no different.

“Hell of a morning, isn’t it, Jin?”

I dropped down beside Magic Johnson, who greeted me with an exhausted face.

Neither of us asked the other how it had gone. We already knew that six hours of searching had come to nothing.

Even so, I spoke up, hoping against hope.

“Johnson.”

“I’m sorry.”

“……”

“We searched every inch of a 700-kilometer radius. We practically threatened Syria and Iraq into cooperating, too. But, damn it…”

The Prophet was gone.

No—he’d vanished.

As if he’d never existed in this world to begin with.

No wonder the elite Hunters who’d joined the search right after me all looked as if they’d seen a ghost.

“We were so close. Where the hell did he run off to?”

The reinforcements had moved quickly.

The reinforcements arrived less than fifteen minutes after J1—a team of roughly two hundred Japanese Hunters—reported an engagement.

The problem was that The Prophet, who’d left the battlefield just before they arrived, couldn’t be found anywhere.

“Jin. As far as I know, there’s only one way to explain this.”

Our eyes met. I murmured quietly,

“Magic.”

“Right. The Prophet is a mage. A mage so skilled he’d deserve to be called a Grand Mage.”

Neither Magic Johnson’s magic nor the Skeleton King’s undead army had found a trace of him. And neither had I.

That left only one possibility.

Magic.

When people encountered something they couldn’t understand, they often called it a miracle or something like magic.

In The Prophet’s case, it was definitely the latter.

He couldn’t really be someone chosen by God, like the brainwashed fanatics who believed in him claimed.

*A mage, huh.*

Huginn’s words suddenly came back to me.

His account that The Prophet seemed like a long-range Hunter.

I’d only half believed him, but this time the scales had to tip in that direction.

The Prophet was probably a mage—and a mage skilled enough to disappear without Magic Johnson noticing.

Or…

*One of his subordinates could be a mage at that level.*

If that was true, it’d be the worst of the worst. Fortunately, Magic Johnson immediately shook his head when he heard my thought.

“That’s not it.”

“I hope you’re right, but there’s still a chance…”

“The Prophet was definitely alone.”

“What?”

The certainty in Magic Johnson’s voice went beyond a simple guess. I asked again instinctively, and the next thing he said explained why.

“There’s a survivor, Jin.”

“……!”

“The only survivor from J1. He woke up not long before you arrived.”

The only survivor.

I couldn’t just sit there and listen after hearing those words. I sprang to my feet and asked Magic Johnson,

“Where is he now?”

* * *

The survivor lay in bed, hooked up to all kinds of medical equipment.

Team Leader Choi and the Skeleton King had been talking beside the bed with serious expressions. They opened their mouths as if to say something when they saw me, but then closed them again.

They must’ve been able to tell from my face alone that the search, which had continued until dawn, had come to nothing.

“That him?”

The Skeleton King immediately understood what I meant and nodded.

“Yeah. The only human left alive among those who were there.”

“Then when I first got to the scene…”

“By then, every last one of them was dead. Not a single wounded person left. That human was in critical condition, too, but he got lucky. You came in, didn’t even listen properly, and left again right away.”

Only then did the frantic scene from earlier return to my mind.

The word *survivor* mixed in among the voices of the people as I’d first headed for the scene—and the Skeleton King trying to say something to me as I left.

“You left before I could say a word. I was about to go after you, but I stopped myself. Something else could’ve happened with me away from here, too.”

The Skeleton King had made the right call. Maybe he’d read the situation even more calmly than I had.

Seeing me bite my lip in silence, Team Leader Choi spoke.

“You both made the right decisions. What matters now is that we have a survivor.”

The loss of well over a hundred lives was tragic, but having someone survive was a miracle.

For him, after surviving that horrific scene. And for all of us.

“He woke up a little while ago—six hours after we found him. According to the healer in charge, he’s had enough potions and is entering the final stage of recovery, so he should be fine.”

I stared at the survivor, who was gazing into space with his mouth hanging open.

He didn’t look all that fine for one thing, and his face seemed somehow familiar.

On top of that, there was the fullness of energy inside him, which I could sense without even needing to check his pulse.

*Wait. Could this guy be…?*

When I realized, I turned my head. Team Leader Choi nodded as if he’d read my mind.

Then a quiet Sound Transmission reached only my ears.

—He’s the person you’re thinking of, Mr. Jin Taekyung. The sole survivor of J1 is Japan’s S-rank Hunter, Yamamoto Genji.

—……!

—It was a close call. From what we can piece together, the reinforcements were just about to arrive. The Prophet must have worried he’d get held up, so he couldn’t make sure the job was done.

The five hundred Hunters who’d arrived as reinforcements had been lucky.

If The Prophet had been a little stupider, or more confident in his own strength, they wouldn’t have escaped death either.

But The Prophet was clever and cautious. He knew the longer he stayed in one place, the greater the threat he’d face.

That was bad news for humanity, but good luck for the people who’d survived.

In that sense, the survivor before me—Yamamoto Genji, staring into space with unfocused eyes—had been blessed with exceptional luck.

Of course, having gone through something similar myself, I didn’t think of it that way.

*Damn it.*

I hated Yamamoto Genji.

If I had to define how I felt about him, it went beyond dislike. It was closer to loathing.

Back when so many people were risking their lives to stop Leviathan, he’d shown up late with the most ridiculous excuse.

The only reason I’d gone out of my way to bring someone like him into the World Hunter Federation was simple: he was an S-rank Hunter.

I’d believed that even if he was a useless bastard, he’d manage to pull his weight at least once.

But no matter what I’d thought of him until now, I had no right to curse Yamamoto Genji.

I had no intention of asking him why he was the only one who’d made it back alive when everyone else was dead.

I was the one who’d sent him—and all of them—into a deathtrap.

*Tap.*

I took Yamamoto Genji’s wrist and sent my internal energy into him.

My Scorching Yang Qi, warm to the touch, flowed through his pulse and into his body. His erratic heartbeat steadied, and a flush of warmth spread across his pale face.

“Yamamoto.”

I spoke his name quietly, and he responded. His cracked lips moved.

“……A-ah.”

I watched him quietly, his mouth opening and closing like he’d forgotten how to speak, as I continued to channel internal energy into him.

How much time passed like that? At last, his eyes came back into focus. Yamamoto Genji looked at me and finally spoke.

“Jo…”

“Jo?”

“Chōsenjin?”[^1]

Wait, this fucking bastard.

[^1]: *Chōsenjin* is a Japanese term for Koreans, used here as an ethnic slur.
```
