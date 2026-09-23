<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0799.txt",
      "sha256": "4e06fc79e5fe4cf34be20334439f68962de87b2f61ab2b38af74dc336f7b11e8",
      "bytes": 13283
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0a2e1d0b140e40533aeb5388dcc86dcf8291cd09590fd658e5d755f0c0779c0b",
      "bytes": 1251
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "97c6dd5161ec61a3fa52be729a8ce6bbdcdcabe92ff1394a89858fdd6b8da351",
      "bytes": 224372
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0c91a46f68865d209c469eaaa21a8fbe393d78f65d755295340195a9840b7314",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "83f7ddcc992627cef706bb365edabea64b8b2518caa7a704c90d3f4390bd4463",
      "bytes": 682
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9d7d3e196722d31f388d599b3456cd1bdb272a544a6b2a47c3f9c0685c9be232",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e55dc578a8c937f588381c22bff945e616928c7542ba5520eca24e4ab0b6260d",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "83f7c663ab2e55be48b8797094b6263c7bc5af8409e447c1cbb0a75e253cc80e",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "39b4222818415132745d7a465af97da12c9117ea557c1ca90a7f7628222777af",
      "bytes": 728
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "4d1ed24ca1f5274bc1ad0b4562a2e916b39151ca9d4a6bb5d4752d81773efe19",
      "bytes": 624
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "872b0745a5170facc445883a263ef7935d27000642a762f633027ebcfff26a44",
      "bytes": 246776
    }
  ],
  "estimated_tokens": 10426
}
-->

# Durable State Update — Chapter 799

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 799. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 799. Profile updates may replace only one
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
  "chapter": 799,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 799,
    "continuity_sources": [799],
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
    "The Prophet escaped the J1 battlefield before reinforcements arrived; a six-hour search across a 700-kilometer radius found no trace of him.",
    "Magic Johnson believes The Prophet acted alone and used magic to evade detection; The Prophet’s location and means of escape remain unknown.",
    "Yamamoto Genji is J1’s sole survivor. He was critically injured, has awakened, and is recovering after Jin treated him.",
    "Jin feels responsible for the Hunters’ deaths because he sent them into danger; he resents Yamamoto but recognizes he has no right to blame him for surviving."
  ],
  "continuity_sources": [
    798
  ],
  "open_questions": [
    "Where is The Prophet, and what magic or other means allowed him to evade detection?",
    "What information can Yamamoto provide about the J1 attack once he has recovered?"
  ],
  "safe_through": 798,
  "temporary_decisions": [
    "Keep magic distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 무인     | **martial artist**                               | Default term                                          |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 테스 | **Tess** | Figure invoked through Taekyung's quotation of “Know thyself.” |
| 정기 | **vital essence** | Energy the Wudang Sect Leader says the monster absorbs from victims. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 팀원 | 팀장 | team member to team leader | Team Leader Kim | casual, familiar, and dialectal | Team members use forms including 햄 and informal greetings when addressing Kim. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 팀장 | 팀원 | freelance team leader to subordinate team member | asshole/punk | insulting-casual | The Team Leader addresses the subordinate with 새꺄 and 인마 while joking and complaining over drinks. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 798
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 798
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild operative and elite fixer personally selected and trained by Michael, now held captive by Jin Taekyung.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 798
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 798
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 797
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 798
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is the mysterious, exceptionally powerful leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 798
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor, now recovering from severe injuries after Jin Taekyung treated him.
- **Personality:** Prideful and easily offended, he is prone to self-aggrandizement and paranoid, self-serving assumptions.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃799화



흑인의 발작 버튼이 ‘N-word’라면 조센징이라는 단어는 한국인 한정 스폐셜 에디션이다.

각종 매체를 통해 일뽕을 과도 섭취한 국내 씹덕들이 조센징 운운하는 것도 기분이 더럽지만, 그 진면목이 드러나는 것은 바로 일본놈한테 직접 들었을 때다.

그러니까, 바로 지금처럼.

“조센징?”

그 마법의 단어가 귓가를 파고든 순간.

아주 먼 옛날, 단군 할아버지로부터 시작된 홍익인간의 의지와 조선 팔도의 정기가 몸속 깊숙한 곳에서 끓어올랐다.

그리고 저 구구절절하고 긴 문장을 네 글자로 압축시키면, 전혀 상관없는 열양지기(熱陽地氣)가 된다.

사실 열받은 김에 아무 말이나 씨부려 봤다.

화아아악.

“어어. 어어어.”

“안 됩니다! 진태경 씨!”

갑작스럽게 발산된 열기에 스켈레톤 킹은 나오지도 않는 침을 꿀꺽 삼켰고, 최 팀장은 미식축구 선수처럼 몸을 날려 나를 붙잡았다.

“아직 때리면 안 됩니다! 환자예요!”

“그렇죠. 최 팀장님 말씀이 맞아요.”

“네, 네. 그러니까…….”

“근데 그게 뭐요.”

“예?”

“놔 봐요. 저 새끼가 꼴 받게 하잖아.”

나는 허리를 단단히 붙잡은 최 팀장의 팔을 떼어 내며 중얼거렸다.

“안중근. 윤봉길. 유관순. 안창호, 김원봉…….”

“헉.”

“무타구치 렌야, 리틀 보이, 팻 맨…….”

“도와주십시오! 저 혼자서는 못 막습니다!”

최 팀장의 지원 요청에 스켈레톤 킹이 담담하게 대답했다.

“어차피 둘이어도 못 막는다.”

“증언은 들어야 할 것 아닙니까!”

“들어야지. 그런데 저놈 막다가 박살 날지도 모르는 이 몸의 아름다운 두개골은 누가 책임진단 말인가.”

“존슨! 미스터 존슨! 도와주십시오!”

쾅!

“누가 감히 나의 최를 괴롭히…… Oh.”

문을 박차고 백기사처럼 나타난 매직 존슨이 눈을 깜빡거렸다.

“이게 도대체 무슨 상황이지?”

“음. 간악한 인간이 원숭이 인간을 죽이려 하고 있다.”

“왓 더 퍽? 왜?”

“간악한 인간에게 조센징이라고 했거든.”

“초우쎈치?”

아직 뜻을 이해하지 못하고 의아해하는 매직 존슨에게, 스켈레톤 킹이 친절한 부연 설명을 덧붙였다.

“이 몸이 아는 바에 의하면, 니거랑 비슷한 뜻이다.”

“머더 퍼커 잽스! 이 빌어먹을 해변의 아들! 진! 당장 놈을 죽여 버려!”

2m가 훌쩍 넘는 거구의 대마도사까지 길길이 날뛰기 시작하자, 최 팀장이 들릴 듯 말 듯한 목소리로 작게 중얼거렸다.

“아니 시팔, 진짜 못 해 먹겠네…….”

“오.”

처음 만났을 때만 해도 뭐 이런 도련님이 다 있나 했었는데, 가끔 가다가 한 번씩 튀어나오는 욕설도 이제는 네이티브가 다 됐다.

제자의 성장을 확인한 스승의 마음이 이런 걸까.

나는 대견한 눈빛으로 최 팀장을 바라보았다.

“많이 느셨네.”

“헛지랄하지 말고 하려던 거나 끝내십시오.”

“진짜 때린다?”

“어차피 막아도 할 거면서 뭘 확인합니까. 그 대신 딱 한 대. 힘 조절해서.”

“오케이.”

최 팀장과의 합의를 끝내고 고개를 돌리자, 그곳에는 한껏 공손해진 야마모토 겐지가 있었다.

“미안합니다. 조금 전에는 경황이 없어서 그만.”

“그래, 나도 미리 미안하다.”

“진 상.”

“아냐, 그냥 조센징이라고 불러. 그래야 나도 마음이 편하지.”

“진 사마!”

프리저 뺨치는 3단 변신을 거친 호칭과 함께, 자리에서 벌떡 일어난 야마모토 겐지가 무릎을 꿇고 머리를 박았다.

“진심으로 사죄드립니다!”

“……너 무슨 도게자 학원 다녔냐?”

실로 완벽하고도 모범적인 도게자 자세.

이 정도면 일본 S급 헌터 검증 테스트에 도게자가 포함되어 있는지 의심이 들 지경이다.

한숨과 함께 고개를 내저은 나는 야마모토 겐지의 뒤통수를 말없이 바라보았다.

젠장.

어쨌거나 내 뜻에 따라 머나먼 중동까지 온 자다.

철수 명령이 떨어졌음에도 잠시 미적거리다가 끝내 팀원들을 전부 잃고 말았지만, 따지고 보면 모든 책임은 통수권자인 내게 있는 거나 마찬가지였다.

야마모토 겐지가 무능한 패장(敗將)이라면, 나는 그런 놈에게 수백 명의 목숨을 맡긴 한심한 지휘관인 셈이니까.

“일어나.”

“…….”

“일어나라고.”

“하, 하잇.”

눈치를 살피던 야마모토 겐지가 정좌를 취했다.

몸이야 포션으로 샤워를 한 덕분에 상처 하나 없었고, 부릅뜬 눈을 보아하니 정신도 멀쩡히 돌아온 모양이다.

“무슨 일이 있었는지 전부 말해. 하나부터 열까지 싹 다.”

머뭇거리던 야마모토 겐지가 바싹 말라붙던 입술을 핥더니, 마침내 입을 열었다.

“무인 수송 차량을 타고 이동하던 중에 그놈이 나타났습니다.”

“선지자?”

“……예.”

선지자. 그 단어에 몸을 부르르 떤 야마모토 겐지가 마른침을 꿀꺽 삼켰다.

“어느 순간 갑작스럽게 차량이 멈추더니, 알 수 없는 기운에 전신이 오싹해지더군요.”

겁쟁이에 얼빠진 놈이지만, 명색이 S급 헌터다. 무언가 잘못되었다는 것쯤은 본능적으로 알아차렸을 것이다.

그런데…….

“차량이 멈췄다고? 저절로?”

“예, 예.”

나와 시선이 마주친 매직 존슨이 입을 열었다.

“마법이야. 마나 간섭으로 무인 수송 차량의 마정석을 정지시킨 게 분명해.”

“아티팩트일 확률은요?”

“물론 그럴 가능성도 있지. 하지만 J1팀에 배정된 차량은 열 대로 알고 있는데, 맞나?”

야마모토 겐지가 대답했다.

“그렇습니다. 모두 동시에 멈췄어요.”

“아티팩트를 이용한 마법은 한계가 분명하지. 놈은 틀림없이 마법사야.”

“마, 맞아요. 맞습니다.”

무언가에 쫓기는 사람처럼 경련하듯 고개를 끄덕인 야마모토 겐지가 말을 이었다.

“제가 똑똑히 봤습니다. 그 섬광, 핏물, 한 번의 손짓에 쓰러지는 사람들…… 그런 광경은 처음이었어요. 주위의 모두가 눈 깜짝할 사이에 죽었습니다. 그건 분명히 마법이었어요.”

그때의 공포를 떠올린 듯, 어느새 그의 손발이 덜덜 떨렸다.

나는 그런 야마모토 겐지를 물끄러미 바라보다가 문득 물었다.

“넌?”

“에?”

“넌, 어떻게 살아남은 거지?”

“그, 그게…….”

간신히 초점을 되찾았던 동공이 흔들린다.

순간 반사적으로 시선을 회피하는 놈의 모습에서, 동료를 잃었다는 슬픔이나 스스로에 대한 분노는 찾아볼 수 없었다.

두려움.

지금 야마모토 겐지에게 느껴지는 감정은 선지자에 대한 두려움과 살아남았다는 안도감뿐이었다.

“도망쳤군. 아니, 도망치려다 실패했나?”

“……!”

이런 개새끼가.

정곡을 찔린 듯 움찔하는 놈의 모습을 보자 속에서 뜨거운 무언가가 울컥 솟구친다.

아마 누군가가 내 어깨를 붙잡지 않았더라면, 증언이고 뭐고 저 겁쟁이 같은 면상에 주먹을 꽂아 넣었을 것이다.

‘빌어먹을.’

씁쓸함과 분노를 삭이기 위해 입술을 잘근잘근 씹었다.

고개를 떨구고 있는 야마모토 겐지를 말없이 노려보던 내가 재차 입을 연 것은, 그로부터 상당한 시간이 흐른 뒤였다.

“그 후에는. 어떻게 됐지?”

고개를 푹 숙인 채 눈깔만 뒤룩뒤룩 굴리고 있던 놈이 조심스럽게 입을 열었다.

“지원 병력이 도착하는 소리를 듣고 자리를 떠났습니다.”

“S급 헌터인 당신을 두고 떠날 만큼 상황이 급했습니까? 분명 선지자도 당신을 살려 두면 걸림돌이 될 거라는 사실을 알고 있었을 텐데요.”

“그, 그건.”

최 팀장이 던진 날카로운 질문에 잠시 머뭇거리던 야마모토 겐지가 입을 열었다.

“아마도 다른 이유가 있어서였을 겁니다.”

“다른 이유라면…….”

“앞서 죽은 우리 팀원들…… 그들에게서 모든 것을 빨아들였습니다.”

“뭐?”

모든 것을 빨아들였다니.

도무지 이해할 수 없는 말에 나를 비롯한 모두가 눈을 크게 뜬 그때, 야마모토 겐지가 다급한 어조로 말을 이었다.

“저, 정말 한 치의 거짓도 없는 사실입니다. 사방에 고여 있던 핏물도 빨아들이고, 죽은 사람들의 몸속에서 희끄무레한 안개 같은 것을 끄집어내 삼켰어요. 그러자 시체가 미라처럼 말라 붙었…….”

순간 뒤통수를 얻어맞은 듯한 충격에, 뒤이어 이어진 목소리는 흐릿하게만 들렸다.

그리고 이러한 충격을 느낀 것은 비단 나 혼자뿐만이 아니었다.

“아냐. 이건, 그런 건 마법이 아니라고.”

신음처럼 중얼거린 매직 존슨이 이마를 문질렀다. 조명 아래에 비친 그의 이마는 어느새 식은땀으로 축축하게 젖어 있었다.

“빌어먹을. 도대체 뭐지? 적어도 내가 아는 한, 인간에게 허락된 마법 중에 그런 끔찍한 건…….”

감정을 따라 격하게 흘러나오던 목소리가 파르르 떨린다.

말을 멈춘 채 석상처럼 굳어 있던 매직 존슨이 천천히 고개를 돌려 어딘가를 응시했다.

아니, 우리 모두가.

그리고 그 시선의 끝에, 한 존재가 있었다.

‘스켈레톤 킹.’

친구이자 등을 맡길 수 있는 전우.

하지만 우리가 본능적으로 녀석을 바라본 이유는, 그의 존재 자체에 선지자에 대한 해답이 있었기 때문이었다.

인간에게 허락되지 않은 마법을 사용하는 자.

대마도사를 단신으로 제거할 실력을 지녔음에도, 단 한 번도 세상에 알려지지 않은 강자.

미카엘 실베르트가 자신의 오른팔인 후긴에게조차 숨겼던 또 하나의 비밀.

‘몬스터(Monster).’

그래.

그것이 바로 선지자의 정체였다.

“노, 놈이 남긴 말이 있습니다.”

선지자라는 이름의 괴물은, 나를 향해 미끼를 던지고 있었다.



* * *



동산처럼 솟아 있는 높은 언덕 위, 터번을 쓴 노인은 그리 멀지 않은 곳에서 뿌옇게 솟아오르는 모래 안개를 바라보았다.

정확히는 모래 사이로 보이는 수십여 대의 차량을.

“제거할까요?”

아무것도 없는 허공에서 들려오는 수하의 목소리에, 노인은 담담하게 되물었다.

“전부 몇이냐.”

“오백여 명 이상으로 예상됩니다.”

“그중 S급 헌터는?”

“저희가 파악한 바에 의하면 없습니다. 만약 있다 하더라도 제가 나선다면 충분히 전멸시킬 수 있고요.”

노인은 억센 수염을 쓰다듬었다. 말없이 생각에 잠겨 있던 그가 입을 연 것은 잠시 후였다.

“놔두어라.”

“하지만 거리가…….”

“하미드, 내 말을 듣지 못했느냐?”

갑작스러운 호명에 잠시 침묵하던 수하가 대답했다.

“죄송합니다, 아미르. 제가 그만 결례를 범했습니다.”

“혈기를 억누르고 곧 다가올 때를 기다려라. 선지자께서 그리 말씀하시지 않았더냐. 모든 것이 그분의 뜻대로 이루어질 것이다.”

노인은 손을 뻗어 허공을 더듬었다. 보이지 않는 무언가가 그들을 이교도들로부터 보호하고 있었다.

우주에 떠 있는 인공위성으로도, 불과 수 킬로미터 남짓한 거리까지 다가왔음에도 그들을 발견할 수 없는 이유는 그 때문이다.

아니, 설령 코앞까지 다가온다 해도 마찬가지다.

그들이 스스로 이 장막을 걷고 나가지 않는 이상 그 누구도 보고 느낄 수 없으며, 만약 그때가 온다면 그건 침입자가 살아 숨 쉬는 마지막 순간이다.

신의 보호라고 생각할 수밖에 없는 이 신비로운 힘.

그들의 신은 당신을 대신하여 선지자를 지상으로 내려보냈고, 선지자는 그들을 이끌고 약속의 땅으로 향할 것이다.

악랄한 이교도를 벌하고, 모든 땅과 바다에 신의 뜻을 바로 세울 터였다.

“조급해하지 말거라. 선지자께서 함께하시는 한, 이 위대한 성전(聖戰)에서 승리하는 것은 우리다.”

“한데 선지자께서는 지금 어디에 계신지…….”

“곧 스스로 임하실 것이니 의심하지 말지어다. 그분께서는 당신께서 펼쳐 놓으신 그물로, 저 이교도들을 하나도 남김없이 들어 올려 신의 곁으로 보내실 것이다.”

“……!”

“인샬라.”

노인은 차오르는 경외심을 느끼며 다시 한번 뇌까렸다.

인샬라.

신의 뜻대로.
```

## Final English reading copy

```markdown
# Chapter 799

If the N-word is the button that sets Black people off, then *Chōsenjin* is the Korean-specific special edition.[^1]

It’s bad enough when Korean weebs who’ve overdosed on Japanophilia start throwing around *Chōsenjin*. But you really see the full horror of it when you hear it straight from a Japanese guy.

Like right now.

“Chōsenjin?”

The moment that magic word pierced my ears—

The will of Hongik Ingan, which had begun with Grandfather Dangun in the distant past, and the vital essence of Korea’s eight provinces surged up from deep within me.

And if you compressed that long-winded sentence into four syllables, you’d get something completely unrelated: Scorching Yang Qi.

Honestly, I was just spouting whatever came to mind because I was pissed off.

*Whoosh!*

“Uh. Uh-oh…”

“Please don’t, Mr. Jin!”

The sudden burst of heat made the Skeleton King swallow saliva he didn’t even have, while Team Leader Choi launched himself at me like a football player and grabbed hold.

“You can’t hit him yet! He’s a patient!”

“Right. Team Leader Choi is right.”

“Yes, yes. So…”

“But so what?”

“Huh?”

“Let go. That bastard’s pissing me off.”

I pried Team Leader Choi’s arms from around my waist and muttered,

“Ahn Jung-geun. Yun Bong-gil. Yu Gwan-sun. Ahn Chang-ho. Kim Won-bong…”

“Gasp.”

“Mutaguchi Renya. Little Boy. Fat Man…”

“Help! I can’t hold him back by myself!”

At Team Leader Choi’s cry for backup, the Skeleton King answered calmly.

“Even the two of us couldn’t stop him.”

“We need to hear his testimony!”

“We do. But who’s going to take responsibility for my beautiful skull if it gets smashed to pieces trying to stop him?”

“Johnson! Mr. Johnson! Help!”

*Bang!*

“Who dares bully my Choi—Oh.”

Magic Johnson burst through the door like a knight in shining armor, then blinked.

“What on earth is going on?”

“Hmm. A wicked human is trying to kill a monkey human.”

“What the fuck? Why?”

“Because the monkey human called the wicked human *Chōsenjin*.”

“Chōsenjin?”

Magic Johnson still looked puzzled, not quite understanding what it meant. The Skeleton King helpfully elaborated.

“As far as I know, it means about the same thing as ‘nigger.’”

“Motherfucking Japs! You goddamn sons of the beach! Jin! Kill that bastard right now!”

Even the hulking Grand Mage, well over two meters tall, had started raging. Team Leader Choi muttered so quietly I could barely hear him,

“Fuck, I really can’t do this anymore…”

“Oh.”

When I’d first met him, I’d thought, *What kind of Young Master is this?* But now, even the occasional swear that slipped out of him sounded native.

Was this how a master felt when he saw his Disciple grow?

I looked at Team Leader Choi with pride.

“You’ve come a long way.”

“Quit screwing around and finish what you were doing.”

“I’m really going to hit him, you know?”

“You were going to do it even if I stopped you, so why ask? Just make it one hit. And go easy.”

“Okay.”

With that settled, I turned around. Yamamoto Genji had become the picture of politeness.

“I’m sorry. I was out of my mind earlier.”

“Yeah. I’m sorry in advance, too.”

“Mr. Jin…”

“No, just call me *Chōsenjin*. That’ll make me feel better.”

“Jin-sama!”

After a three-stage transformation in how he addressed me that would’ve put Frieza to shame, Yamamoto Genji sprang to his feet, dropped to his knees, and pressed his forehead to the floor.

“I sincerely apologize!”

“……Did you go to a dogeza academy or something?”

It was a perfect, textbook dogeza.

At this point, I was starting to wonder whether dogeza was part of the Japanese S-rank Hunter certification test.

I sighed and shook my head, then stared silently at the back of Yamamoto Genji’s head.

Damn it.

Whatever else, he’d come all the way to the Middle East on my orders.

He’d hesitated for a while even after the order to withdraw, and in the end he’d lost every member of his team. But if you looked at it closely, I was more or less responsible for all of it as the one in command.

If Yamamoto Genji was an incompetent defeated general, then I was a pathetic commander who’d entrusted the lives of hundreds of people to a man like that.

“Get up.”

“……”

“I said, get up.”

“Y-yes.”

Yamamoto Genji cautiously sat back on his heels.

His body was completely free of injuries, thanks to the potion shower he’d had. And judging by his wide-open eyes, his mind seemed to be working properly again, too.

“Tell me everything that happened. From beginning to end. Don’t leave anything out.”

Yamamoto Genji hesitated, licked his parched lips, and finally began.

“We were traveling in unmanned transport vehicles when he appeared.”

“The Prophet?”

“……Yes.”

At the word *The Prophet*, Yamamoto Genji shuddered and swallowed.

“At some point, the vehicles suddenly stopped, and an unknown force made my whole body go cold.”

He was a coward and a fool, but he was still an S-rank Hunter. He must’ve instinctively sensed that something was wrong.

But…

“The vehicles stopped? On their own?”

“Y-yes.”

Magic Johnson met my gaze and spoke.

“It was magic. He must have used mana interference to shut down the Magic Gems powering the unmanned transport vehicles.”

“What are the odds it was an artifact?”

“That’s certainly possible. But I understand J1 had ten vehicles assigned to them. Is that right?”

Yamamoto Genji answered.

“That’s right. They all stopped at once.”

“Magic used through an artifact has clear limitations. He’s definitely a mage.”

“R-right. That’s right.”

Yamamoto Genji nodded spasmodically, like someone being chased, and continued.

“I saw it clearly. The flash of light, the blood, people falling at a single gesture… I’d never seen anything like it. Everyone around me died in the blink of an eye. It was definitely magic.”

As if he were reliving the terror of that moment, his hands and feet began to tremble.

I stared at Yamamoto Genji for a while, then suddenly asked,

“What about you?”

“Huh?”

“How did you survive?”

“Th-that…”

His pupils, which had just managed to refocus, wavered.

He reflexively avoided my gaze. There was no grief over the loss of his comrades in him, no anger at himself.

Fear.

The only things Yamamoto Genji felt now were fear of The Prophet and relief at having survived.

“You ran. No—did you try to run and fail?”

“……!”

You son of a bitch.

When he flinched as if I’d hit the mark, something hot surged up inside me.

If someone hadn’t grabbed my shoulder, I would’ve punched that cowardly face of his, testimony or no testimony.

*Damn it.*

I bit down on my lip, trying to swallow the bitterness and anger.

I silently glared at Yamamoto Genji, his head bowed. A long time passed before I spoke again.

“What happened after that?”

The man had his head lowered, his eyes darting around. He cautiously began to speak.

“He heard the reinforcements arriving and left.”

“Was the situation so urgent that he had to leave you behind, an S-rank Hunter? The Prophet must have known you’d be a problem if he let you live.”

“Th-that…”

Yamamoto Genji hesitated for a moment at Team Leader Choi’s sharp question, then answered,

“He must have had another reason.”

“Another reason…?”

“He sucked everything out of my teammates who’d died before me.”

“What?”

Sucked everything out of them?

As the rest of us stared at him, unable to make sense of his words, Yamamoto Genji hurriedly continued.

“I-I swear there isn’t a single lie in what I’m saying. He sucked up the pools of blood all around us, too. He pulled something like a pale mist out of the dead people’s bodies and swallowed it. After that, the corpses dried up like mummies…”

The shock hit me like a blow to the back of the head. The words that followed came through only faintly.

And I wasn’t the only one stunned.

“No. This… That isn’t magic.”

Magic Johnson muttered as if he were groaning and rubbed his forehead. Under the lights, his forehead had grown damp with cold sweat.

“Damn it. What the hell was it? As far as I know, there’s no magic permitted to humans that could do something that horrifying…”

His voice, which had been surging out with his emotions, trembled.

Magic Johnson stopped speaking and stood frozen like a statue. Then he slowly turned his head and looked somewhere.

No—all of us did.

And at the end of our gazes stood one being.

*The Skeleton King.*

My friend. A comrade I could trust with my back.

But the reason we’d instinctively looked at him was that the answer to The Prophet lay in his very existence.

Someone who used magic not permitted to humans.

A powerful being, capable of taking out a Grand Mage single-handedly, whose strength had never once been revealed to the world.

Another secret Michael Silbert had hidden even from Huginn, his right-hand man.

*A monster.*

That was right.

That was what The Prophet really was.

“He left behind a message.”

The monster called The Prophet had been dangling bait in front of me.

* * *

On a tall hill rising like a mound, an old man in a turban watched a hazy cloud of sand billow up not far away.

More precisely, he watched the dozens of vehicles visible through the sand.

“Shall we eliminate them?”

At his subordinate’s voice, which came from empty air, the old man asked calmly,

“How many are there?”

“We estimate more than five hundred.”

“Any S-rank Hunters among them?”

“Not that we’ve been able to determine. Even if there are, I could wipe them all out if I went in.”

The old man stroked his coarse beard. He fell silent in thought, and only after a short while did he speak.

“Leave them be.”

“But the distance…”

“Hamid, did you not hear me?”

After a moment’s silence at the sudden call, the subordinate answered,

“I’m sorry, Amir. I was out of line.”

“Restrain your impatience and wait for the time soon to come. Did The Prophet not say as much? Everything will unfold according to his will.”

The old man reached out and felt around in the air. Something invisible was protecting them from the infidels.

That was why even satellites in orbit couldn’t detect them—and why the infidels couldn’t find them despite drawing within a few kilometers.

No, the infidels wouldn’t find them even if they came right up to them.

Unless they lifted this veil and went out on their own, no one could see or sense them. And if that moment came, it would be the last moment their intruders spent alive.

This mysterious power could only be thought of as divine protection.

Their god had sent The Prophet down to earth in his place, and The Prophet would lead them to the promised land.

They would punish the wicked infidels and set God’s will straight across every land and sea.

“Do not be impatient. As long as The Prophet is with us, we will be victorious in this great holy war.”

“But where is The Prophet now…?”

“He will come of his own accord soon. Do not doubt it. With the net he has laid, he will gather up every last one of those infidels and send them to God.”

“……!”

“Inshallah.”

Feeling his reverence swell, the old man murmured it once more.

Inshallah.

God willing.

[^1]: *Chōsenjin* is a Japanese term for Koreans, used here as an ethnic slur.
```
