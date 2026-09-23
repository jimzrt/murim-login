<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0791.txt",
      "sha256": "83ef5873803b6c024c258825361d254d649aaaebfc0b95ae6d618e2bf438e26a",
      "bytes": 13552
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "de993ff44b1ec84531d31d2ed5231f9efdc62fe0f41e1c741533093c61e3ad63",
      "bytes": 1222
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b107ad8b032275926005814226705b9c99fd04942849ff404275ebe5d6ff70cc",
      "bytes": 223952
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "72744a9f47de2e440c7c7c78b84160b15efca4501c30a17a9f6435eb684fec52",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b4c5e99b4bad9bb594ca4dfe89a6c431863270a94ac68c70d25521c192a000d9",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dbb2734261cc177209cd5c4b6b02b44154ea30e1ae3ab4b5350dfcd9ac8b2f6d",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "b159a660d16ac7bcec10b9e2e22c9e25025b981db288385c2c416e5d923ff905",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "c3b29934913bee7454ba031a8662272142f0be0f108d85f43891afb4ed324a95",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ce37c4566435af26d5f9e0f8c3be8f18f1a8865dea42552bf6278747296528c8",
      "bytes": 244692
    }
  ],
  "estimated_tokens": 9901
}
-->

# Durable State Update — Chapter 791

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 791. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 791. Profile updates may replace only one
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
  "chapter": 791,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 791,
    "continuity_sources": [791],
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
    "Michael Silbert is dead; the World Hunter Federation’s operation against his associates led to arrests of major political and business figures.",
    "Jin Taekyung has accepted the World Hunter Federation’s appointment as Alliance Leader.",
    "The Main Quest [Cataclysm] is incomplete and now requires Jin to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is in a cave in the Middle East. The Federation is mobilizing against them at Jin’s order; their followers estimate at least 100,000 Hunters are approaching.",
    "Footage from a surviving National Assembly camera has been released publicly, exposing the truth behind the Federation’s operation and winning broad public support."
  ],
  "continuity_sources": [
    789,
    790
  ],
  "open_questions": [
    "Can Jin eliminate The Prophet before the Main Quest’s unspecified time limit expires?",
    "Is The Prophet the beginning of the approaching Cataclysm, and what will it involve?"
  ],
  "safe_through": 790,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Do not treat the nightmare’s fire and rift as established future events."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 습득               | **Acquired**                   |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 대한민국 | **Korea** | Country reference. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 790
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 790
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 790
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 790
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 790
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃791화



내가 아는 바에 의하면, 중동(中東)이 세계에서 차지하는 비중은 생각보다 크다.

좁게는 서아시아 일대부터, 넓게는 북아프리카의 국가들까지 포함하는 광활한 면적.

게다가 대격변 이후 적극적인 이주 정책으로 인하여 중동에 거주하는 인구는 무려 3억 명을 넘어섰다.

뿐만이 아니다.

중동 지역을 먹여 살린 유전(油田)은 지금까지도 제 몫을 톡톡히 해내고 있었고, 골고루 분포된 게이트에서는 석유를 밀어내고 필수 자원으로 급부상한 마정석을 얻을 수 있다.

‘물론, 그렇게 습득한 마정석 중 절반은 뒷구멍으로 빠져나가겠지만.’

그 동네가 원래 그렇다.

딱히 비리를 파헤칠 만큼 힘 있는 사회단체도, 정부 부처도 없다 보니 들어오는 게 있어도 뒤로 줄줄 새는 것이다.

중동에는 무소불위의 부와 권력을 움켜쥔 왕가(王家)가 존재하고 테러 단체가 버젓이 활동하며, 혁명 지도자로 시작하여 독재자로 진화한 위선자도 있다.

그리고 그들에게 있어 법이란 단물이 빠지면 언제든지 뱉어 버릴 수 있는 껌에 불과하다.

‘미카엘 실베르트는 그 점을 정확히 파고들었고.’

마정석의 밀반입 및 미정제는 국제법에도 명시된 엄청난 중죄지만, 빈틈은 얼마든지 있다.

특히 테러 단체와 반군이 득실거리는 중동 및 아프리카에는 더더욱.

하지만 이미 죽은 놈은 더 이상 문제가 되지 않는다.

다만…….

‘살아 있는 놈이 문제지.’

툭.

나는 태블릿 PC를 내려놓고 눈가를 문질렀다. 몇 시간째 활자만 쳐다보고 있으니 피로가 몰려왔다.

아니, 어쩌면 줄곧 뇌리를 떠나지 않는 세 글자 때문일지도.

‘선지자.’

얼굴도 모르는 놈을 떠올리며 창밖을 바라봤다.

먹구름이 가득한 하늘을 가로지르는 항공기의 날개와 쏟아지는 빗줄기 사이로, TV를 통해 들었던 목소리가 천둥처럼 울려 퍼지는 듯했다.



‘신의 뜻을 따라, 우리는 멈추지 않는다. 오늘을 시작으로 너희를 심판하고 벌할 것이다.’



놈은 누구일까.

분명 변조되지 않은 목소리임에도 불구하고 성별, 나이도 제대로 분간할 수 없었다. 푹 눌러쓴 로브로 가린 얼굴은 물론이다.

‘굳이 그렇게 가렸다는 건, 이미 얼굴이 알려진 놈이라는 뜻일까?’

그럴 확률이 높겠지만, 이것조차 확실치 않다. 선지자의 존재는 저 창밖의 먹구름을 닮아 있었다.

“기상이 좋지 않군요.”

갑작스럽게 들려온 목소리에, 나는 여전히 창밖을 바라보며 대답했다.

“그러게요. 아무리 봐도 비행하기에 좋은 날씨는 아닌데.”

“이 정도면 그런 수준이 아니라, 최악이죠.”

“혹시 선지자가 기상청에 끄나풀 심어 둔 거 아니에요?”

“왜 그렇게 생각하십니까?”

“왜 그렇게 생각하냐니. 암살 각 날카롭게 잡혔잖아요, 이거.”

털썩, 옆자리에 앉은 최 팀장이 입을 열었다.

“제가 알고 있는 두 가지 사실을 말씀드리자면, 첫째로 공항 예보는 정확했습니다. 이건 마력 수치로 인한 기후 변동일 뿐이고요. 그리고 둘째로 제가 선지자라면 그런 헛수고는 안 할 겁니다.”

“어째서요?”

“이 비행기가 추락한다고 해도, 진태경 씨는 살아남을 테니까요.”

“……오.”

“아닙니까?”

“글쎄요. 아직은 비행기 추락 사고를 겪어 보질 못해서.”

사실 이것만으로도 황당한 대답이다. 이런 날씨와 높이에서 추락한다면 죽는 게 당연하니까.

아마 최 팀장도 나와 비슷한 생각을 한 것이 분명했다.

고개를 절레절레 흔든 그의 시선이 문득 테이블 위에 놓인 태블릿 PC를 향했다.

“다 보셨습니까?”

“네. 지긋지긋할 정도로 여러 번.”

추가된 부분이 있긴 하지만, 절반 정도는 이미 눈에 익을 대로 익은 자료다.

세계 헌터 연맹이 설립되기 전, 며칠 밤을 새워 가며 읽고 또 읽었던 내용이었으니까.

미카엘 실베르트와 관련된 것이었으니 당연하게도 선지자와 중동에 관한 정보 역시 빠질 수 없었다.

“이 자료들에 대해 어떻게 생각하십니까.”

“글쎄요. 적어도 세 가지는 알 것 같네요.”

나는 활자가 빽빽하게 들어찬 태블릿 PC를 노려보며 말을 이었다.

“단기간에 선지자를 찾아내기에는 중동이 더럽게 넓고, 놈이 지독하게 잘 숨어 있다는 것.”

“그럼 마지막 하나는…….”

“그 빌어먹을 새끼가, 엄청난 양의 정제되지 않은 마정석을 갖고 있다는 거죠.”

그래, 그게 문제다.

전 세계에 무차별적으로 테러를 가하던 선지자는 미카엘 실베르트가 죽은 이후에도 잠잠했고, 대중들은 놈이 겁을 먹었다고 생각하며 안심하는 중이다.

하지만…… 그래서 더 불안했다.

지금의 이 분위기가. 폭풍 전의 고요함이.

‘더 큰 뭔가를 노리고 있다. 분명히.’

지금까지와는 다른 메인 퀘스트, 그리고 시스템이 격변(激變)이라 명명할 정도의 중요성.

바로 그런 이유로 나는 즉각 세계 헌터 연맹을 움직였다.

혹시 모를 추가 테러 및 몬스터 웨이브를 방지하기 위한 인원을 제외하더라도, 중동으로 파견한 병력만 무려 10만.

그들 한 사람, 한 사람이 헌터라는 것을 감안한다면 실로 엄청난 전력이다.

당장 전 세계에서 인정받는 헌터 강국인 대한민국조차, 개개인의 수준을 떠나 그 정도로 많은 헌터를 동원할 수는 없으니까.

일각에서는 처음부터 너무 과한 병력을 운용하는 것 아니냐는 말도 흘러나왔지만, 그런 헛소리는 나오자마자 쏙 들어갔다.

현재 세계 헌터 연맹의 권위와 힘은 그 정도로 막강하다.

지구상의 거의 모든 나라가 속한 UN 총회가 동의했고, 인류 전체가 우리를 지지한다.

미국이 스스로를 세계 경찰이라 ‘자칭’했다면, 세계 헌터 연맹은 말 그대로 자타공인이자 언터처블이다.

미국을 필두로 한 서방 세력과 사사건건 부딪쳤던 러시아조차 연맹과의 적극 협조를 약속하며 거부 반응을 보이는 중동 국가에 경고장을 날렸으니까.

- 뒤지기 싫으면 길 터라.

외교 전문은 길었지만, 한 줄로 요약하자면 저 내용이다.

러시아 종신 대통령인 블라디미르 푸린은 테러로 인해 붉은 광장이 무너진 것을 매우 유감스럽게 생각하고 있었고, 얼마 전 열렸던 UN 총회 당시 미카엘 실베르트의 편에 섰던 몇몇 중동 국가를 벼르고 있었다.

그러니 뭐, 별수 있겠나.

10만이나 되는 헌터들의 방문을 그리 달가워하지 않던 중동 지도자들은 고작 몇 시간도 지나지 않아 자신들의 영공과 영해를 활짝 열어젖혔다.

국제적인 질타도 질타지만, 햇빛이 쏟아지는 어느 날 아침에 방사능 홍차를 마시게 될 수도 있었으니까.

하지만 전 세계가 연맹에 협조하고 있다고 해서, 선지자가 저절로 잡히는 것은 아니었다.

“수색은 어디까지 진행됐습니까?”

내 물음에 최 팀장이 즉각 대답했다.

“모두가 각자의 자리에서 최선을 다하고 있지만, 현재로서는 어디에서도 별다른 특이점을 발견하지 못했습니다. 면적도 광범위하고, 수색을 시작한 지 이제 고작 하루밖에 지나지 않았으니까요.”

알고 있다. 그것이 지금 내가 중동으로 향하는 가장 큰 이유 중 하나니까.

그러나 성급한 질문이라도, 계속해서 물어볼 수밖에 없었다.

“예상 소요 시간은요?”

“최악의 경우에는 60일 이상입니다. 연맹의 헌터는 물론이고, 뒤이어 합류한 연합군을 총동원했을 경우 나온 수치입니다.”

“……60일.”

“다시 한번 말씀드리지만, 최악의 경우에 한해서입니다. 총력을 기울인다면 시간을 단축할 가능성은 충분합니다.”

글쎄. 과연 그럴까.

나는 별다른 대꾸는 하지 않았지만, 마음속에서 꿈틀거리는 불안감을 느꼈다.

‘호락호락한 놈이 아니야.’

선지자는 연맹이 설립되기 이전에도 전 세계의 감시망을 피했던 놈이다.

남미의 마약왕이나, 한참 선배 격인 오사마 빈 라덴을 아득히 뛰어넘은 사상 최악의 테러리스트.

누군가는 그런 놈을 두 달 안에 잡을 수 있다는 것만으로도 생각할 수 있겠지만…… 적어도 나는 아니다.

‘두 달이면 너무 늦어.’

짐작대로라면 현재 놈의 수중에는 엄청난 양의 마정석이 있다. 정제되지 않은, 그래서 더욱 위험한 시한폭탄이.

그 폭탄이 언제쯤 터질지는 아무도 모른다.

한 달. 혹은 보름 뒤. 어쩌면…….

‘당장 내일일 수도 있겠지.’

그리고 그 폭탄이 터지는 날. 내게 주어진 메인 퀘스트의 제목처럼 격변(激變)이 시작되리라는 것쯤은 어렵지 않게 예상할 수 있었다.

그렇게 된다면 지금까지 선지자가 벌인 테러와 비견될 만한, 아니 어쩌면 그 이상의 재앙이 전 세계를 휩쓸 것이다.



‘이제 자네 차례야. 어디 한 번 있는 힘껏 발버둥 쳐 보게. 나는 저 위에서 내려다보고 있을 테니.’



문득 귓가에 맴도는 누군가의 목소리.

이제야 알겠다.

미카엘 실베르트가 죽기 직전 유언처럼 남겼던 그 말의 진짜 의미를.

하지만 누구도 막을 수 없을 것만 같던 그놈을 지옥 밑바닥으로 처박았듯이, 나는 이번에도 싸울 준비가 되어 있었다.

확신에 가까운 짐작과 함께.

‘아직 준비되지 않은 건, 선지자 역시 마찬가지다.’

배고픈 사람이 먹음직스러운 음식을 앞에 두고 참을 이유는 없는 법.

선지자는 아직 폭탄을 터트릴 준비를 끝마치지 못했을 가능성이 높다.

요리가 완성되기 전에 발각되지 않기 위하여 숨을 죽이고, 납작 엎드려 있을 뿐이다.

‘그 전에 찾아내야 한다. 반드시.’

마음속으로 뇌까린 나는 최 팀장을 바라보았다.

“화물은요? 얌전히 있습니까?”

“화물이라고 하시면, 아.”

화물이 무엇을 뜻하는지 깨달은 최 팀장이 쓴웃음을 지으며 대답했다.

“조용히 잘 있습니다. 가끔씩 말썽을 피우긴 하지만.”

“잘 지켜보세요. 선지자에 대해 알아내야 할 게 산더미니까.”

“알겠습니다.”

고개를 끄덕인 나는 창밖으로 시선을 돌렸다.

어느새 저 멀리, 흐릿한 먹구름 사이로 어둠 속에서 환히 빛나는 도시가 가까워지고 있었다.



* * *



냉기가 흐르는 사막의 밤.

누가 봐도 감탄이 흘러나올 만한 외모를 지닌 청년이 깜깜한 하늘을 바라보며 중얼거렸다.

“……방금 뭔가 지나간 것 같은데. 그 녀석인가.”

“예?”

“아니다. 그냥 혼잣말이야. 그보다 어디에서 통신이 끊겼다고?”

청년, 스켈레톤 킹의 반응에 고개를 갸웃거리던 샤오 쉔이 대답했다.

“동남쪽으로 30km 정도 더 이동해야 합니다. 스 선생님.”

“스 선생…… 그렇게 부르지 말라고 했던 것 같은데.”

“앗. 죄송합니다. 킹 선생님.”

“……여전히 이상하긴 한데, 묘하게 기분이 나쁘지 않군.”

“감사합니다!”

“좋아하지 마라. 이 애송이 인간아.”

투덜거리긴 했지만, 목적지를 향해 이동하는 스켈레톤 킹의 기분은 앞서 했던 말처럼 썩 나쁘지 않았다.

아니, 오히려 내심 기쁘기까지 했다.

‘저 꼬마 녀석은 이 몸이 아무렇지도 않나?’

정체가 밝혀진 직후, 스켈레톤 킹은 어딜 가나 따라다니는 시선을 느꼈다.

누군가는 노골적인 적대감까지는 아니어도 경계 어린 눈빛으로 그를 주시했고, 또 다른 누군가는 환하게 웃으며 호의를 표했다.

간혹 어떤 종류의 호기심은, 그 자체만으로도 부담감을 느끼게 만든다.

스켈레톤 킹은 그런 이유로 홀로 수색 작업을 벌이는 것을 택했다. 차라리 혼자가 편하니까. 사람들의 시선에서 잠시라도 벗어날 수 있으니까.

하지만 중국에서 왔다는 저 꼬맹이는 아무렇지도 않게 합류하더니, 지금까지도 함께하고 있었다.

‘간악한 인간의 말에 의하면 착한 짱깨는 죽은 짱깨뿐이라고 했는데, 역시 극소수지만 예외는 있군.’

내심 흐뭇하게 웃은 스켈레톤 킹은 샤오 쉔과 함께 목적지에 도착했다.

약간의 숲과 사막이 뒤섞인 그곳에서, 한 시간 전 수색대 1개 분대의 통신이 끊겼었다.

“여기냐?”

“예. 틀림없습니다, 킹 선생님.”

“주위에 아무것도 안 보이는데. 확실한 거 맞…….”

그 순간.

눈살을 찌푸린 채 주위를 둘러보던 스켈레톤 킹의 눈동자가 부릅떠졌다.

“……저게 뭐야?”
```

## Final English reading copy

```markdown
# Chapter 791

As far as I knew, the Middle East played a bigger role in the world than most people realized.

It covered a vast area, from Western Asia in the narrow sense to the countries of North Africa in the broadest.

And since the Great Cataclysm, active resettlement policies had pushed the population living in the Middle East past a staggering three hundred million.

That wasn’t all.

The oil fields that had sustained the region were still doing their part, and the Gates scattered throughout the area provided Magic Gems—a resource that had rapidly overtaken oil in importance.

*Of course, half the Magic Gems obtained that way probably disappear through back channels.*

That was just how things worked around there.

There weren’t any powerful civic groups or government departments capable of digging into corruption, so even when money came in, it leaked right back out.

In the Middle East, royal families held wealth and power without limit. Terrorist groups operated openly, and hypocrites who began as revolutionary leaders had evolved into dictators.

To them, the law was nothing more than gum they could spit out whenever they’d sucked all the flavor from it.

*Michael Silbert knew exactly how to exploit that.*

Smuggling in Magic Gems and leaving them unrefined were grave crimes explicitly covered by international law, but there were plenty of loopholes.

Especially in the Middle East and Africa, where terrorist groups and rebels were everywhere.

But a man who was already dead was no longer a problem.

It was the ones still alive…

*They’re the problem.*

*Tap.*

I set down the tablet and rubbed my eyes. Staring at text for hours had worn me out.

Or maybe it was because of those three syllables that had never left my mind.

*The Prophet.*

Thinking about someone whose face I didn’t even know, I gazed out the window.

Between the plane’s wings cutting across the cloud-choked sky and the rain pouring down, it felt as if the voice I’d heard on TV were rumbling like thunder.

> “Following God’s will, we will not stop. Starting today, we will judge and punish you.”

Who was that bastard?

Even though the voice hadn’t been altered, I couldn’t make out their gender or age. Their face was hidden, too, beneath a hood pulled down low.

*Does the fact that they hid their face so carefully mean they’re already recognizable?*

That was likely, but even that wasn’t certain. The Prophet’s existence was like the storm clouds outside the window.

“The weather’s bad.”

At the sudden voice, I kept looking out the window and answered.

“It sure is. Doesn’t look like good flying weather at all.”

“It’s not just bad. It’s the worst.”

“Think The Prophet planted a mole at the weather service?”

“What makes you think that?”

“What do you mean, what makes me think that? This is a perfect setup for an assassination.”

Team Leader Choi dropped into the seat beside me and spoke.

“I can tell you two things I know. First, the airport forecast was accurate. This is just a weather shift caused by magical power. And second, if I were The Prophet, I wouldn’t bother with something so pointless.”

“Why not?”

“Even if this plane crashed, Mr. Jin Taekyung would survive.”

“…Huh.”

“Am I wrong?”

“Who knows? I’ve never been in a plane crash before.”

Even that was a ridiculous answer. A crash from this height, in weather like this, should obviously be fatal.

Team Leader Choi had probably thought something similar to me.

He shook his head, then his gaze fell on the tablet lying on the table.

“Have you read it all?”

“Yes. Enough times to be sick of it.”

Some of the material had been added, but about half of it was already familiar to me.

Before the World Hunter Federation was founded, I’d spent several nights reading through those same documents over and over.

Since they were related to Michael Silbert, it was only natural that the information on The Prophet and the Middle East was included.

“What do you make of these materials?”

“Hard to say. I think I can tell at least three things.”

I glared at the tablet, crammed with text, and continued.

“The Middle East is damn huge, so finding The Prophet quickly will be tough—and they’re damn good at hiding.”

“Then the last one is…”

“That bastard has an enormous amount of unrefined Magic Gems.”

Right. That was the problem.

The Prophet, who’d launched indiscriminate terrorist attacks around the world, had gone quiet even after Michael Silbert’s death. The public thought they were scared and had started to relax.

But…

That only made me more uneasy.

This mood. This calm before the storm.

*They’re planning something bigger. I’m sure of it.*

A Main Quest unlike any I’d seen before, and one so important the System had named it *Cataclysm*.

That was exactly why I’d mobilized the World Hunter Federation without delay.

Even after accounting for the personnel needed to prevent further terrorist attacks and monster waves, we’d sent a full hundred thousand troops to the Middle East.

Considering that every one of them was a Hunter, that was an enormous force.

Even Korea, a Hunter powerhouse recognized around the world, couldn’t mobilize that many Hunters—not even if you ignored the level of each individual Hunter.

Some people had murmured that we were deploying far too many troops from the start, but that nonsense stopped as soon as it started.

That was how great the World Hunter Federation’s authority and power were now.

The UN General Assembly, to which nearly every country on Earth belonged, had given its approval, and all of humanity supported us.

If the United States had *called itself* the world’s police, the World Hunter Federation was recognized as such by everyone—and untouchable.

Even Russia, which had clashed at every turn with the Western powers led by the United States, had promised full cooperation with the Federation and sent a warning to the Middle Eastern countries showing resistance.

—If you don’t want to die, clear a path.

The diplomatic cable was long, but that was the gist of it in one line.

Furin, Russia’s president for life, was deeply aggrieved that the terrorist attack had destroyed Red Square. He’d also been itching to settle the score with several Middle Eastern countries that had sided with Michael Silbert at the recent UN General Assembly.

So, what could they do?

The Middle Eastern leaders, who hadn’t been thrilled about a hundred thousand Hunters showing up, had thrown open their airspace and territorial waters within a few hours.

International condemnation was one thing, but they could also wake up one sunny morning and find themselves drinking radioactive tea.

But just because the whole world was cooperating with the Federation didn’t mean The Prophet would fall into our hands on their own.

“How far has the search gotten?”

Team Leader Choi answered at once.

“Everyone is doing their best, but so far, no one has found anything unusual. The area is vast, and it’s only been a day since the search began.”

I knew. That was one of the biggest reasons I was heading to the Middle East now.

Even so, I couldn’t help asking again, even if it was premature.

“How long do you expect it to take?”

“In the worst case, more than sixty days. That estimate assumes we mobilize every Federation Hunter as well as all the allied forces that joined afterward.”

“…Sixty days.”

“Again, that’s only in the worst case. If we put everything we have into it, we have a good chance of shortening that time.”

Who knew? Would we, really?

I didn’t reply, but I could feel the unease stirring inside me.

*They’re not going to be easy to deal with.*

The Prophet had evaded the eyes of the entire world even before the Federation was founded.

The worst terrorist in history, far beyond the South American drug lords or even his much older predecessor, Osama bin Laden.

Some people might have thought it was amazing we could catch someone like that within two months…

But I wasn’t one of them.

*Two months is too late.*

If my guess was right, The Prophet had an enormous quantity of Magic Gems in their possession. Unrefined, and therefore all the more dangerous—a ticking time bomb.

No one knew when that bomb would go off.

A month from now. Maybe two weeks. Or…

*It could be tomorrow.*

And the day that bomb went off, it was easy enough to imagine the Cataclysm beginning, just as the Main Quest I’d been given was titled.

If that happened, a disaster on par with—no, possibly even worse than—the terrorist attacks The Prophet had carried out so far would sweep across the world.

> “It’s your turn now. Let’s see you struggle with everything you’ve got. I’ll be watching from up there.”

A voice suddenly echoed in my ears.

Now I understood.

The true meaning of the words Michael Silbert had left behind like a last will before he died.

But just as I’d sent that bastard, who’d seemed impossible to stop, plunging into the depths of hell, I was ready to fight again.

With a suspicion that was close to certainty.

*The Prophet isn’t ready yet, either.*

A hungry person has no reason to hold back when delicious food is right in front of them.

There was a good chance The Prophet hadn’t finished preparing to set off the bomb.

They were probably lying low, holding their breath so they wouldn’t be discovered before the cooking was done.

*I have to find them before that happens. No matter what.*

I muttered to myself, then looked at Team Leader Choi.

“What about the cargo? Is it behaving?”

“The cargo? Oh.”

Realizing what I meant, Team Leader Choi replied with a wry smile.

“It’s being quiet. Though it does cause trouble every now and then.”

“Keep a close eye on it. We’ve got a mountain of things to find out about The Prophet.”

“Understood.”

I nodded and turned back to the window.

In the distance, a city shone brightly in the darkness, drawing closer through the dim storm clouds.

* * *

A cold night in the desert.

A young man with an appearance that would make anyone who saw him gasp in admiration gazed up at the dark sky and murmured.

“…I think something just passed by. Was that him?”

“What?”

“Nothing. Just talking to myself. Anyway, where did we lose contact?”

Xiao Shen tilted his head at the Skeleton King’s reaction, then answered.

“About thirty kilometers farther southeast, Mr. S.”

“Mr. S… I thought I told you not to call me that.”

“Oh. Sorry, Mr. King.”

“…It still sounds strange, but for some reason, I don’t mind it.”

“Thank you!”

“Don’t get excited, you young human brat.”

He grumbled, but the Skeleton King was in a pretty good mood as he headed toward their destination—just as he’d said.

No, he was actually quite pleased.

*That little kid doesn’t mind me at all?*

Ever since his identity had been revealed, the Skeleton King had felt people’s eyes following him wherever he went.

Some watched him with wary eyes, if not outright hostility, while others smiled brightly and treated him with kindness.

Sometimes, even a certain kind of curiosity could be burdensome in itself.

For that reason, the Skeleton King had chosen to search alone. It was better that way. At least he could get away from people’s eyes for a while.

But this little brat who’d come from China had joined him without a second thought, and he’d been right by the Skeleton King’s side ever since.

*That devious human once said the only good Chink was a dead Chink, but it seems there are exceptions, even if they’re few and far between.*

Smiling to himself, the Skeleton King reached the destination with Xiao Shen.

The area was a mix of sparse woods and desert. An hour earlier, an entire squad of the search party had lost contact there.

“This the place?”

“Yes. No doubt about it, Mr. King.”

“I don’t see anything around here. Are you sure—”

At that moment.

The Skeleton King had been frowning as he surveyed the area, but his eyes suddenly flew open.

“…What’s that?”
```
