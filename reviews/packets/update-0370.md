<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0370.txt",
      "sha256": "7b57ce66da591b76454aa348bf285dbb515675b2206686f7e19e19b5cc402380",
      "bytes": 14929
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c28b92327dbd87bb09c70d38e4832dc9b819b336c48dfbf74e7fdd1b65416279",
      "bytes": 1662
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6555cac231424dcd06e81c434fc7ccbd23718de4108a7517e631eef840404b9e",
      "bytes": 3543
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2c312975fd717b1edd3bae9803ab6527a1a5c1d79ea71c7412e1bc47461308a4",
      "bytes": 5010
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a64c2fe283cb32e54d79e5dabdd572939300d3097bd09e6b8cb86f7b9c2fb1de",
      "bytes": 23754
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bdae616c899ebdcfb1105b2e93b0addab94bba58be071e5bbaee02bdd1b01178",
      "bytes": 1979
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 11360
}
-->

# Durable State Update — Chapter 370

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 370. Keep at most
2 continuity_sources. Use only chapter
numbers through 370. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
both Korean keys must occur in the source. Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.

Return this exact shape:

{
  "chapter": 370,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 370,
    "continuity_sources": [370],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Mukyung recognizes Taekyung as a First Rate martial artist standing before the Peak realm and is astonished by his transformation over three years.",
    "Taekyung's spar with Mukyung ends with Mukyung's victory and the destruction of the pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and is publicly credited with protecting Taekyung, with rumors that he will become the next Master of the Gatekeeper Pavilion.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Chapters 66–369 have no accepted local English in this expedition; do not invent that range.",
    "Chapter 370 is the next chapter to translate from Korean source. Parked Chapters 374–375 must not be used as foreshadowing."
  ],
  "continuity_sources": [
    65
  ],
  "open_questions": [
    "The identity of the assassin who attacked Taekyung and Hyuk Mujin remains unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion."
  ],
  "safe_through": 369,
  "temporary_decisions": [
    "This expedition backfills Chapters 370–373 and skips accepted translation of Chapters 66–369.",
    "When current Korean source conflicts with Chapter 65 continuity or this seed, the current source wins.",
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun.",
    "Use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형님 in Taekyung's deferential speech."
  ],
  "version": 1
}
```

## Expedition bridge dossier

# Expedition Seed Dossier

This dossier is intentionally conservative. It orients the Chapter 370 catch-up.
It is not a substitute for translating Chapters 66–369, and it must not leak
plot from parked Chapters 371–375.

## Hard boundary

- Accepted English continuity is reliable through Chapter 65.
- Chapters 66–369 are skipped and have no accepted local English in this
  expedition.
- Chapter 370 is the next chapter to translate. Its Korean source is the
  authority for every beat in that chapter.
- Parked accepted translations of Chapters 374–375 exist in this branch. Do not
  read them, their reviews, or old 371–373 bridge summaries while drafting
  370–373.
- When the Korean source of the current chapter conflicts with this dossier or
  with Chapter 65 continuity, the current source wins. Do not invent missing
  backstory; preserve ambiguity and flag an unresolved continuity issue.

## Opening position for Chapter 370

Chapter 370's source opens at the Sichuan Tang Clan. About seven days have
passed since the Three-Sect Bloodbath. The clan's gates, long closed, are open
to reconstruction and to orthodox guests. Do not assert later names, ranks,
quests, or outcomes that the current chapter has not yet shown.

## Translation guardrails

- Treat the Korean source as authoritative for every line of the chapter being
  translated.
- Do not back-project titles, names, ranks, or skills from parked later
  chapters or web searches into the skipped range without current-source
  evidence.
- Use established local terminology where it exists from Chapters 0–65.
- For terms first evidenced in the current source, follow the ledger and
  first-use rules. Record new bindings through the normal update stage.
- The light, self-mocking first-person voice and the source's jokes remain
  important, but missing continuity must never be filled by invented exposition.

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 독룡각 | **Poison Dragon Pavilion** | Pavilion led by Tang Horyong |
| 당호룡 | **Tang Horyong** | Acting Family Head of the Sichuan Tang Clan |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 경천신니 | **Heaven-Shaking Divine Nun** | Murder victim named alongside Tang Sadok |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 구파일방 | **Nine Sects and One Gang** | Major orthodox organizations |
| 오대세가 | **Five Great Families** | Major orthodox families |
| 소림혈사 | **Shaolin Bloodbath** | Earlier attack that galvanized orthodox Murim |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 만독지환 | **Myriad Poison Ring** | Item Taekyung considers taking before departure |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 동봉 | **Dongbong** | Name or designation associated with the Divine Physician. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 사죄와 용서 | **Atonement and Forgiveness** | Hidden Quest completed by Taekyung. |
| 당문의 은인 | **Benefactor of the Tang Clan** | Title acquired by Taekyung. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 명성               | **Fame**                       |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 당사독 | **Tang Sadok** | Poison King and Family Head of the Sichuan Tang Clan |
| 삼문혈사 | **Three-Sect Bloodbath** | Recent attack on three major orthodox sects |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 미미 | **Mimi** | Tang Sadok's snake and longtime companion; temporarily entrusted to Cheongpung. |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 65
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃370화



사천당문은 예로부터 폐쇄적이기로 유명한 가문이었다.

어지간히 이름난 명사조차 쉽게 드나들 수 없고, 출가외인(出嫁外人)이 가문의 무공과 기밀을 누출할까 염려한 탓에 데릴사위를 들여 당씨 성을 잇게 했다.

이러한 방식으로 수백 년을 존속한 사천당문의 문이 활짝 열린 것은, 불과 칠 주야 전의 일이었다.

“거기, 기둥 똑바로 세워!”

“셋 세면 당긴다. 자. 하나, 둘-!”

단단한 체구의 인부들이 밧줄을 당기고, 돌과 목재를 실어나른다.

너른 부지 위, 검붉은 핏자국이 남아 있는 주춧돌 위로 건물이 서서히 형태를 갖춰 나갔다.

거기서 멀리 떨어진 어느 곳에서는 수십의 승려들이 모여 염불(念佛)을 외었다.

“원아진생무별염 아미타불독상수 심심상계옥호광…….”

파르라니 깎은 머리, 정기가 서린 눈빛을 한 승려의 정체는 아미파의 여승들이었다.

그들의 앞에는 수많은 목관이 불길에 휩싸여 타오르고 있었다.

“부디 극락왕생하시길. 그대들의 절개와 넋을 잊지 않겠습니다.”

몇 번의 낮과 밤이 바뀌었지만, 불길은 아직도 꺼지지 않았다.

삼문혈사(三門血史)에서 유명을 달리한 희생자들은 그만큼 많았고, 그중에서도 특히 사천당문이 입은 인명손실은 극심했다.

“후우…….”

“묘령사태, 피곤해 보이시는데 잠시라도 쉬시는 것이…….”

“아닙니다. 명진 도장. 해야 할 일을 하는 것뿐이니 괘념치 않으셔도 됩니다. 계속하시지요.”

파리한 안색의 중년 여승을 바라보던 도사가 무겁게 고개를 끄덕였다.

잠시 후 검을 찬 무림인들이 수십여 개의 목관을 들고 줄지어 걸어왔다.

그중에는 청성파의 도사도 있었고, 중소 문파의 제자들도 있었으며 땟국물이 줄줄 흐르는 거지도 있었다.

그런 그들의 뒤로 헐레벌떡 뛰어가는 것은 한 무리의 의원들이었다.

“갑자기 환자가 피를 토했다니. 안정된 것 아니었나?”

“그걸 알면 내가 지금 여기 있겠소? 심각한 내상을 입은 건 분명한데 도무지 무슨 증상인지…….”

“빨리 흩어져서 신의를 모셔와라!”

아미의 여승과 청성의 도사, 개방의 거지들과 크고 작은 문파에서 파견한 무인들. 거기에 더해 목수, 석공과 의원을 비롯한 양민들까지.

헤아릴 수 없이 많은 이가 사천당문의 경내를 누비며 각자의 역할을 충실히 하고 있었다.

높이 솟은 전각. 활짝 열린 창 너머로 이 광경을 지켜보던 젊은 거지, 궁기방은 피곤한 듯한 목소리로 중얼거렸다.

“살다 살다 이런 광경을 볼 줄은 몰랐군. 그것도 사천당문에서.”

그러자 침상에 누워 있던 혁무진이 대꾸했다.

“보지만 말고 가서 좀 도우십쇼. 후개라고 농땡이만 피우지 말고.”

“농땡이?”

눈을 부릅뜬 궁기방이 자신의 몸을 가리켰다.

새하얀 붕대로 칭칭 감긴 상반신. 한쪽 다리에는 임시로 부목을 댔다. 삼괴를 상대하면서 얻은 영광의 상처였다.

“지금 내 꼴을 보고도 그런 말이 나오나? 이게 농땡이야? 어?”

“궁 소협만 다쳤습니까?”

콧방귀를 뀐 혁무진이 보란 듯이 지렁이처럼 몸을 꿈틀거렸다.

궁기방과는 달리 전신이 붕대로 감겨 있는 그의 모습은 목내이(木乃伊)를 연상케 했다.

“이 정도는 다쳐야지 아, 이 녀석 고생 좀 했구나. 하는 겁니다. 아시겠어요?”

“……!”

궁기방은 몸을 부르르 떨었다. 분명히 크게 다치지 않은 건 자신의 무공이 더 높았다는 반증인데, 왠지 모르게 진 기분이다.

“난 붕대를 다섯 번이나 갈았다!”

“전 살아 있는 게 기적입니다. 그리고 그거야 몸이 하도 지저분하니까 그런 것 아닙니까. 참다못한 의원이 궁 소협 때 밀어 주다가 지쳐서 실신했다던데. 사실이에요?”

“…….”

“됐습니다. 더 말 섞어 봤자 입 냄새만 나지. 말이 나왔으니 말인데, 다음에는 이빨도 좀 닦아 달라고 하십쇼. 궁 소협이랑 대화할 때마다 저잣거리 똥개 엉덩이에 대고 말하는 기분이에요.”

실로 악랄한 혓바닥이 아닌가.

잠시 할 말을 잃었던 궁기방은 천장을 바라보며 한탄했다.

“삼괴가 저놈을 죽였어야 했는데.”

“어? 선 넘네?”

“도대체 너 같은 놈이 어떻게 그 격전에서 살아남은 건지, 아직도 모르겠다.”

“정 궁금하면 우리 조장님이랑 이 년만 붙어 다녀 보시든가.”

“……그건 사양하지.”

늘 티격태격하는 궁기방과 혁무진이 유일하게 일치하는 의견이 있다면, 그건 바로 진태경에 관한 문제였다.

세상의 온갖 평지풍파(平地風波)를 합쳐 놓은 듯한 존재. 그 어떤 위기 속에서도 용케 살아남는 끈질긴 생명력과 집념.

그리고 이제는 아득하게 느껴질 만큼의 무위를 갖춘 진태경을 보고 있노라면, 도무지 이게 같은 사람인가 싶을 정도였다.

‘그런 사람이 하나 더 있긴 하지.’

‘그래, 저놈.’

같은 생각을 떠올린 두 사람의 고개가 동시에 한 방향을 향해 움직였다.

“미미, 회오리치기!”

취리릭!

“잘했어, 미미! 이번에는 공중 날기!”

취릭?

“아, 이건 안 되는구나. 그럼 이번에는…….”

혁무진과 궁기방은 생각했다. 뱀에게 공중을 날라고 시키는 저 괴상한 청년이, 정말 검성의 후인이자 기련삼괴 중 가장 강하다는 일괴를 단신으로 쓰러트린 화산신룡이 맞는지.

“저기, 궁 소협.”

“왜.”

“원래 살짝 맛이 가야 초절정 고수가 될 수 있는 겁니까?”

“……몰라. 이제는 나도 정말 모르겠다.”

궁기방은 대답을 회피했다.

그의 스승도 제법 괴팍한 축에 드는 성격이지만, 진태경이나 청풍만큼은 아니었다.

검성과 화왕을 보면 제자들이 스승을 닮은 건지도 몰랐다.

“그런데 저 뱀은 도대체 뭐예요?”

“저렇게 큰 뿔이 달린 뱀은 이무기 빼면 하나뿐이야. 천년독각사.”

“어렸을 때 본 영물백과(靈物百科)에서는 온통 검은 빛을 띤 엄청난 독물이라던데.”

청풍이 외쳤다.

“미미. 엎드려!”

취릭!

“저걸 보면 독물이 아니라 그냥 동물 같은데.”

“제 말이요.”

“그런데 청 소협은 왜 여기 있는 거야? 별로 다치지도 않았더만.”

“아까 밖에서 큰 소리 나는 거 못 들었습니까? 그거 청 소협이 도와준답시고 나섰다가 전각 부순 거래요.”

“……아.”

동시에 할 말을 잃은 두 사람은 나란히 침상에 누워 천장을 바라봤다.

구 할에 달하는 건물이 파손되는 와중에도 용케 형태를 유지한 전각은, 중요한 환자들을 모아 둔 임시 의방(醫方)으로 쓰이는 중이었다.

어디선가 흘러들어 온 탕약 냄새를 맡던 혁무진이 문득 중얼거렸다.

“꿈 같네요.”

“그러게.”

삼문혈사가 일어난 그 날로부터 어언 칠 주야.

사천 무림이 결집하여 펼친 천라지망에 사천 곳곳을 피로 물들인 암천의 흑의인들은 대부분 죽거나 사로잡혔고 감쪽같이 사라졌던 삼괴마저 정체 모를 괴인에 의해 붙잡혔다. 그로써 짧은 전란은 막을 내렸다.

하지만…….

“이게 끝이 아닐 것 같은데. 궁 소협은 어떻게 생각합니까?”

“그걸 말이라고. 여기서 끝나면 내 손바닥에 장을 지지겠다.”

비단 두 사람뿐만이 아닌 모두가 느끼고 있는 위기였다.

고작 두 달 남짓한 시간 동안 하남과 사천이 피로 물들었다.

곧 삼문혈사에 관한 소식이 대륙 끄트머리까지 퍼진다면 천하인들은 깨닫게 될 것이다.

어느새 암천이라는 먹구름이 코앞까지 다가왔음을.

바야흐로 부정할 수 없는 난세(亂世)의 시작이었고, 영웅들은 그러한 난세 속에서 태어나는 법이었다.

혁무진의 시선이 자연스럽게 닫혀 있는 문 너머를 향했다.

“궁 소협이 생각하기에 조장님께서 언제쯤 깨어나실 것 같습니까?”

“글쎄, 나라고 방도가 있나. 우선 문경의 말에 의하면 아무 문제도 없다 하니 기다리는 수밖에.”

“말이 나왔으니 말인데, 문경이가 나이에 비해서 실력이 좋긴 하지만 조장을 맡기기에는 좀 그렇지 않습니까?”

“신의도 바쁘시니까 그런 거겠지. 적천강 대협께서도 기력을 회복 중이시고, 당사독 대협 같은 중환자들도 워낙 많다 보니까 어쩔 수 없다.”

“이해는 합니다. 이해는 하는데, 아무리 신의의 제자라고 하지만 문경이는 좀……. 그 어린 것이 알면 얼마나 알겠습니까?”

우려 섞인 혁무진의 말에 청풍이 번쩍 고개를 쳐들었다.

“어어, 하지 마세요. 죽어요.”

“청 소협?”

“방금 하셨던 말, 문 할. 아니 문경이 앞에서는 특히 하지 마세요.”

“예? 갑자기 그게 무슨…….”

“안 돼요. 정말 안 돼요.”

“……?”

혁무진과 궁기방이 어리둥절한 얼굴로 서로의 얼굴을 바라보는데 청풍이 갑자기 헙, 하고 숨을 삼켰다.

“미미야! 어디 갔어, 미미야!”

잠깐 눈을 뗀 사이 사라진 천년독각사를 청풍이 애타게 찾던 그 순간, 굳게 닫힌 문 너머에서 억눌린 외침이 터져 나왔다.

“컥! 야, 이 뱀 새끼야!”

세 사람의 시선이 허공에서 부딪쳤다.

동시에 한 사람을 부르는 여러 개의 이름이 전각 밖까지 쩌렁쩌렁 울려 퍼졌다.

“은인!”

“조장님!”

“진태경!”

그 외침에 밖에서 각자의 일을 하고 있던 사람들 사이에서도 일대 소란이 일어났다.

“방금 들었나?”

“혹시 깨어나신 건가?”

“이 소식을 장문인께 알려라! 어서!”



* * *



악몽을 꿨다.

한 치 앞도 보이지 않는 칠흑 같은 어둠 속, 한 마리의 뱀이 천천히 목을 조 여오는 꿈을.

숨이 막혔고, 눈앞이 새하얗게 물들었다.

그리고 다음 순간, 나는 참았던 숨을 토해 내며 눈을 떴다.

“커헉!”

취릭.

“……?”

취릭? 이거 뭐여, 시벌.

삼 초간의 사고 정지.

마침내 악몽의 정체를 깨달은 나는 목에 칭칭 감겨 있는 뱀의 뿔을 잡아챘다.

“야, 이 뱀 새끼야!”

천년독각산지 미미쨩인지, 이름이 뭐였건 상관없다. 오늘부터 이 새끼 이름은 뱀술이다.

“넌 오늘부터 이슬만 먹고 산다. 참이슬.”

붕붕 휘둘러 힘차게 바닥에 내리찍으려던 그때, 굳게 닫혀 있던 문이 박살 나며 한 사람이 뛰쳐 들어왔다.

“은인-!”

청풍의 쩌렁쩌렁한 외침에 골이 울린다.

녀석의 등 뒤로 지렁이처럼 꿈틀거리는 혁무진과 한 발로 콩콩 뛰어오는 궁기방이 보였다.

“조장님!”

“진태경!”

“……너희는 꼴이 왜 그 모양이냐.”

혁무진이 힘차게 몸을 튕기며 대답했다.

“삼괴. 그 미친 노괴가 절 이렇게 만들었습니다.”

궁기방이 친절하게 부연설명을 덧붙였다.

“살아남은 것이 천운이다. 혁무진 저 미친놈이 흙에 돌을 섞어서 삼괴에게 던졌거든. 때마침 칠선자가 나서서 막아 주지 않았다면 오체분시 됐을 거다.”

“……?”

아니, 삼괴는 또 누구고 칠선자는 누구야. 김선자는 나 고등학생 때 학생주임 이름인데…….

‘이런 미친놈들.’

지하 뇌옥에서 살아남았다는 안도감도 잠시, 나는 두통을 느끼며 이마를 감쌌다.

분명히 신의의 거처에 처박혀 있으랬는데, 그새를 못 참고 기어 나와 죽자고 싸운 모양이다.

목숨을 건졌기에 망정이지, 죽었으면 어쩔 뻔했나.

“너희들 죽고 싶어서 환장했냐? 또 무슨 사고를 친 거야?”

“……?”

“……?”

“뭐, 왜?”

이놈들 표정이 왜 이래?

청풍을 제외한 우리 세 사람은 어리둥절한 얼굴로 시선을 교환했다.

“무슨 문제 있냐?”

“당연히 있지.”

“조장님이 시키셨잖아요. 가서 아미파 구원하라고.”

첫 번째 대답은 궁기방이고, 그다음은 혁무진이었다.

둘다 헛소리라 나는 짐짓 눈살을 찌푸렸다.

“무슨 소리야. 내가?”

“예. 분명히 문경이한테 그렇게 들었는데. 혹시 머리 다치셨어요?”

그럴 리가.

눈을 뜨자마자 느낄 수 있었다. 전신에서 끓어오르는 강대한 기운.

눈 앞에 펼쳐진 시야와 나를 둘러싼 대자연의 기운이 또렷하고 생생하게 느껴졌다.

‘이것이 초절정…….’

당장이라도 이 힘을 시험해 보고 싶다. 지금쯤 산더미처럼 쌓여 있을 시스템 메시지도.

물론 그전에 이런 헛소리를 계속 듣는 대신 한 가지를 물어봐야 했다.

“다들 무사하냐?”

내가 말한 ‘다들’에 누가 포함되어 있는지는 녀석들도 알고 있을 것이다.

환하게 웃은 청풍이 대답 대신 커다란 창문을 활짝 열어젖혔다.

“은인께서 직접 확인하세요.”

나는 홀린 것처럼 천천히 창가를 향해 걸어갔다.

따스한 봄바람이 얼굴을 스쳤고, 이상할 만큼 조용한 공기가 창밖으로 고개를 내민 나를 반긴다.

“아.”

아래를 내려다본 나는 할 말을 잃었다.

그곳에 사람들이 있었다.

여승, 도사, 목수와 같은 장인으로 보이는 이도 있고 새하얀 의복을 걸친 의원도 있다. 헤아릴 수 없을 만큼 무수히 많은 시선에 담긴 감정은 하나였다.

‘경외.’

다음 순간, 그들은 약속이라도 한 것처럼 예를 취했다.

누군가는 포권을 취하고, 누군가는 작게 고개를 숙였으며, 누군가는 깊이 엎드려 절했다.

동시에 하나가 된 거대한 목소리가 흘러나왔다.

“열화신룡(烈火神龍)을 뵙습니다!”

한 줄기의 전율이 정수리부터 발끝까지 관통하며 훑어내린 그 순간.

띠링.



- 당신의 업적과 명성은 중원 전체에 울려 퍼질 것입니다.

- 새로운 별호를 획득했습니다!



귓가를 파고드는 시스템 알림과 함께, 나는 저 멀리 보이는 한 사람을 발견했다.

- 잘했다.

나는 적천강을 따라 웃었다.
```

## Final English reading copy

```markdown
# Chapter 370

The Sichuan Tang Clan had been famous for its closed-off ways since time immemorial.

Even renowned figures could not easily come and go as they pleased. Fearing that daughters who married out might leak the clan’s martial arts and secrets, the clan instead took in live-in sons-in-law and had them carry on the Tang surname.

The gates of the Sichuan Tang Clan, which had survived for hundreds of years in that fashion, had been thrown wide open only seven days ago.

“Hey, you! Set that pillar straight!”

“We’ll pull when I count to three. Ready. One, two—!”

Stocky laborers hauled on ropes and carried stones and lumber from place to place.

Across the broad grounds, buildings were slowly taking shape atop foundation stones still stained dark red with blood.

Farther away, dozens of monks gathered and chanted Buddhist prayers.

“May I be reborn without a single thought of separation. Amitabha alone as my companion. Deeply and profoundly bound, the radiance of the jeweled vessel…”

With their heads shaved close and their eyes gleaming with vitality, the monks were nuns of the Emei Sect.

Countless wooden coffins burned before them, engulfed in flames.

“May you be reborn in the Pure Land. We will never forget your integrity and your souls.”

Several days and nights had passed, but the flames had yet to die down.

That was how many victims the Three-Sect Bloodbath had claimed. And among them, the Sichuan Tang Clan had suffered particularly devastating losses.

“Whew…”

“You look tired, Satae Myo Ryeong. You should rest, even if only for a little while…”

“No, Daoist Myeongjin. I am merely doing what needs to be done, so please do not concern yourself. Let us continue.”

The Daoist gazed at the pale-faced middle-aged nun, then nodded heavily.

A short while later, martial artists with swords at their waists came marching in a line, carrying several dozen wooden coffins.

Among them were Daoists from the Qingcheng Sect, disciples from various mid-sized and minor sects, and even a beggar with grime running down his face.

A group of physicians hurried along behind them.

“I heard a patient suddenly started vomiting blood. Wasn’t he stable?”

“If I knew that, would I be here right now? He clearly suffered severe internal injuries, but I can’t figure out what his symptoms mean…”

“Hurry! Spread out and bring the Divine Physician!”

Emei nuns, Qingcheng Daoists, beggars from the Beggars’ Sect, and martial artists dispatched from sects both great and small. Alongside them were commoners, including carpenters, stonemasons, and physicians.

Countless people moved through the grounds of the Sichuan Tang Clan, each faithfully carrying out their assigned role.

From a tall pavilion, a young beggar watched the scene through a wide-open window and muttered in a weary voice.

“I never thought I’d live to see something like this. And in the Sichuan Tang Clan, of all places.”

Hyuk Mujin, lying on a bed nearby, answered him.

“Don’t just watch. Go help. Just because you’re the Future Beggar Chief doesn’t mean you can loaf around.”

“Loaf around?”

Gung Gibang opened his eyes wide and pointed at himself.

His upper body was tightly wrapped in snow-white bandages, and one leg had been temporarily fitted with a splint.

They were glorious wounds earned while fighting Samgoe.

“Look at me! You still have the nerve to say that? This is loafing around? Huh?”

“Are you the only one who got hurt, Young Hero Gung?”

Hyuk Mujin snorted and deliberately wriggled his body like an earthworm.

Unlike Gung Gibang, he was wrapped in bandages from head to toe, making him resemble a mummy.

“You have to be hurt this badly before people say, ‘Ah, that kid must have really been through hell.’ Do you understand?”

“…”

Gung Gibang’s body trembled.

The fact that he had not been seriously injured was clearly proof that his martial arts were superior, yet for some reason, he felt as if he had lost.

“I changed my bandages five times!”

“Being alive is a miracle for me. And that’s only because your body was so filthy. I heard the physician who finally lost patience and tried to scrub you down passed out from exhaustion. Is that true?”

“…”

“Forget it. Talking to you will only leave a bad smell in my mouth. Since we’re on the subject, ask them to brush your teeth next time, too. Every time I talk to you, it feels like I’m speaking straight into the ass of a stray dog in the marketplace.”

What a vicious tongue.

Gung Gibang was speechless for a moment, then looked up at the ceiling and lamented.

“Samgoe should have killed that bastard.”

“Hey. That’s crossing a line.”

“I still don’t understand how someone like you survived that battle.”

“If you’re really curious, try following our squad leader around for two years.”

“…”

“I’ll pass.”

If there was one thing the constantly bickering Gung Gibang and Hyuk Mujin agreed on, it was Jin Taekyung.

A man who seemed to embody every disturbance in the world. A man with the tenacious vitality and dogged determination to somehow survive every crisis.

And now Jin Taekyung possessed martial prowess so far beyond what they remembered that, whenever they looked at him, they wondered whether he was really the same person.

*There is one more person like that.*

*Yeah. That guy.*

The two men arrived at the same thought, and their heads turned in the same direction.

“Mimi, spin like a whirlwind!”

Whrrr!

“Good job, Mimi! This time, fly through the air!”

Ssssk?

“Ah, so this one doesn’t work. Then how about…”

Hyuk Mujin and Gung Gibang wondered whether the bizarre young man ordering a snake to fly was truly the heir of the Sword Saint and the Huashan Divine Dragon who had single-handedly defeated Ilgoe, the strongest of the Qilian Samgoe.

“Say, Young Hero Gung.”

“What?”

“Do you have to be slightly unhinged to become a Supreme Peak master?”

“…”

“I don’t know. I really don’t anymore.”

Gung Gibang evaded the question.

His master was fairly eccentric himself, but not to the same degree as Jin Taekyung or Cheongpung.

*Maybe disciples really do take after their masters.*

Or perhaps that was simply how the disciples of the Sword Saint and the Fire King turned out.

“But what is that snake, exactly?”

“There’s only one snake with horns that big, apart from an imugi.[^1] A thousand-year one-horned snake.”

“An encyclopedia of spirit creatures I read as a child said it was an enormous, pitch-black venomous creature.”

Cheongpung shouted.

“Mimi! Lie down!”

Ssssk!

“Looking at that, it doesn’t seem venomous. It just seems like an animal.”

“That’s exactly what I mean.”

“Then why is Young Hero Cheong here? He doesn’t look very injured.”

“Didn’t you hear that loud noise outside earlier? They say Young Hero Cheong went out to help and ended up destroying a pavilion.”

“…”

The two men fell silent at the same time. Then they lay side by side on their beds and stared at the ceiling.

Although nearly nine-tenths of the buildings had been damaged, this pavilion had somehow remained intact. It was currently being used as a temporary treatment room for important patients.

Hyuk Mujin caught the scent of a medicinal decoction drifting in from somewhere and suddenly muttered,

“It feels like a dream.”

“Yeah.”

Seven days and nights had passed since the day of the Three-Sect Bloodbath.

The Sichuan Murim had united and cast an inescapable net across the region. Most of Dark Heaven’s black-clad men, who had painted various parts of Sichuan red with blood, had been killed or captured. Even the Samgoe, who had vanished without a trace, had been caught by a mysterious figure.

And with that, the brief war had come to an end.

But…

“I don’t think this is over. What do you think, Young Hero Gung?”

“Do you really have to ask? If this ends here, I’ll fry my own palm.”

It was a crisis everyone felt—not just the two of them.

In barely two months, Henan and Sichuan had been stained with blood.

Once news of the Three-Sect Bloodbath spread to the farthest reaches of the continent, the people of the world would realize it.

The Dark Heaven storm cloud had already arrived right before their eyes.

The beginning of an age of chaos that could no longer be denied.

And heroes were born in such troubled times.

Hyuk Mujin’s gaze naturally drifted toward the closed door.

“When do you think our squad leader will wake up?”

“Who knows? Do I look like I have any way of knowing? According to Mungyeong, there’s nothing wrong with him, so all we can do is wait.”

“Since we’re on the subject, Mungyeong may be skilled for his age, but isn’t he a little too young for us to entrust our squad leader to him?”

“The Divine Physician is busy, I suppose. Great Hero Jeok Cheongang is still recovering his strength, and there are so many other critical patients, including Great Hero Tang Sadok. It can’t be helped.”

“I understand. I do understand, but even if he is the Divine Physician’s Disciple, Mungyeong is a bit… How much could that child possibly know?”

At Hyuk Mujin’s worried words, Cheongpung abruptly lifted his head.

“Don’t. You’ll die.”

“Young Hero Cheong?”

“What you just said—don’t say it in front of Grandfa—no, especially not in front of Mungyeong.”

“What? Why are you suddenly saying—”

“No. Really, don’t.”

“…”

Hyuk Mujin and Gung Gibang exchanged bewildered looks. Then Cheongpung suddenly sucked in a breath.

“Mimi! Where did you go, Mimi?”

At that moment, just as Cheongpung began desperately searching for the thousand-year one-horned snake that had disappeared during the brief time he looked away, a muffled shout burst from beyond the firmly closed door.

“Gack! Hey, you snake bastard!”

The three men’s gazes collided in midair.

At the same time, several different names for one person rang through the pavilion and echoed outside.

“Benefactor!”

“Squad Leader!”

“Jin Taekyung!”

The shouts caused a commotion among the people outside, who had been busy with their respective tasks.

“Did you hear that?”

“Could he have woken up?”

“Report this to the Sect Leader! Quickly!”

* * *

I had a nightmare.

In an abyss of pitch-black darkness where I could not see even an inch ahead, a snake slowly tightening around my neck.

I couldn’t breathe, and my vision washed white.

Then, in the next moment, I opened my eyes and exhaled the breath I had been holding.

“Guh-ack!”

Ssssk.

“…”

*Ssssk? What the fuck is this?*

Three seconds of complete mental shutdown.

At last, I realized what the nightmare had been. I grabbed the horn of the snake tightly wrapped around my neck.

“Hey, you snake bastard!”

I didn’t care whether its name was Thousand-Year One-Horned Snake, Mimi-chan, or whatever else.

From today onward, this bastard’s name was Snake Wine.

“You’re living on nothing but dew from now on. Cham Isul.[^2]”

I swung it around, preparing to slam it forcefully onto the floor, when the firmly closed door exploded inward and someone charged through.

“Benefactor!”

Cheongpung’s thunderous shout made my skull ring.

Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg.

“Squad Leader!”

“Jin Taekyung!”

“…”

“Why do you all look like that?”

Hyuk Mujin answered while vigorously bouncing his body.

“Samgoe. That insane old monster did this to me.”

Gung Gibang helpfully added an explanation.

“It’s a miracle you’re alive. That crazy Hyuk Mujin mixed dirt with rocks and threw it at Samgoe. If Chilseonja hadn’t stepped in and blocked it at just the right moment, he would have been dismembered.”

“What?”

*Who the hell are Samgoe and Chilseonja? Kim Sunja was the name of my high-school dean of students…*

*These fucking lunatics.*

My relief at surviving the underground prison lasted only a moment before I felt a headache coming on and pressed a hand to my forehead.

I had clearly told them to hole up at the Divine Physician’s residence, but apparently they had been unable to sit still and had crawled out to fight to the death.

Thank God they had survived. What would I have done if they had died?

“Were you idiots desperate to die? What kind of trouble did you cause this time?”

“…”

“…”

“What? Why?”

Why did they look like that?

The three of us—everyone except Cheongpung—exchanged bewildered glances.

“Is there a problem?”

“Of course there is.”

“You told us to go save the Emei Sect, Squad Leader.”

The first answer came from Gung Gibang. The second came from Hyuk Mujin.

They were both talking nonsense, so I deliberately frowned.

“What are you talking about? I did?”

“Yes. That’s definitely what I heard from Mungyeong. Did you hit your head?”

No way.

I could feel it the moment I opened my eyes: a powerful qi boiling throughout my entire body.

The world spread out before me and the qi of nature surrounding me felt clear and vivid.

*So this is the Supreme Peak realm…*

I wanted to test this power immediately. And the System messages that must have piled up by now.

But before I could keep listening to this nonsense, there was one thing I needed to ask.

“Is everyone safe?”

They all knew who I meant by *everyone*.

Cheongpung threw open the enormous window instead of answering.

“See for yourself, Benefactor.”

As if possessed, I slowly walked toward the window.

A warm spring breeze brushed my face. An oddly quiet atmosphere greeted me as I leaned out and looked beyond the window.

“Ah.”

I looked down and was rendered speechless.

There were people gathered below.

Nuns, Daoists, and people who appeared to be craftsmen, such as carpenters. Physicians wearing brilliant white garments.

The emotion contained in the countless gazes turned toward me was singular.

*Awe.*

The next moment, they all paid their respects as if they had rehearsed it.

Some gave a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves deeply.

At the same time, one enormous voice rose as though from a single throat.

“We pay our respects to the Blazing Fire Divine Dragon!”

A shiver pierced me from the crown of my head to the tips of my toes.

Ding.

> **System**
>
> - Your achievements and Fame will resound throughout the Central Plains.
> - You have acquired a new epithet!

Along with the System notification ringing in my ears, I spotted someone in the distance.

“Well done.”

I smiled back at Jeok Cheongang.

[^1]: An *imugi* is a serpent from Korean legend said to become a dragon.

[^2]: *Cham Isul* is a Korean soju brand whose name literally means “true dew.”
```
