<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0372.txt",
      "sha256": "3bd015ac74499d3033844d9af47194aee4cc27c84a55d1896ee767bb1736bbca",
      "bytes": 13084
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1fb298fe79dd43d08bd77b0f6f00e9f80a03165ffe4035cdfaf264319cc4df28",
      "bytes": 1624
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "555a8e90504fbbf7fae8708b05289615b30c1e083db0bd562dade2aea4fe96db",
      "bytes": 5567
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "a46956759200960eb652ff822583ddb3da698389abced0e2e6f05fd85c69c3b8",
      "bytes": 494
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d91479ac259c5b4a45f4107ab429a7897a8efa7c3c0c7bf1ab9b0942043981f4",
      "bytes": 3302
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 11055
}
-->

# Durable State Update — Chapter 372

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 372. Keep at most
2 continuity_sources. Use only chapter
numbers through 372. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 372,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 372,
    "continuity_sources": [372],
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
    "Seven days after the Three-Sect Bloodbath, the Sichuan Tang Clan is open for reconstruction, funerals, medical treatment, and assistance from orthodox allies and commoners.",
    "Most of Dark Heaven's attackers in Sichuan are dead or captured, and Samgoe has been captured by an unidentified figure; the immediate conflict has ended but a broader age of chaos is beginning.",
    "Jin Taekyung has awakened as a Supreme Peak martial artist and is publicly recognized by the epithet Blazing Fire Divine Dragon.",
    "Mungyeong is the martial artist known as the Slaughter Saint.",
    "The Qingcheng and Emei Sect Leaders have asked Jin Taekyung and Jeok Cheongang to investigate a strange formation connected to Samgoe's interrogation.",
    "A message hawk has been sent to Henan for a reply concerning the situation."
  ],
  "continuity_sources": [
    370,
    371
  ],
  "open_questions": [
    "The identity of the mysterious figure who captured Samgoe remains unknown.",
    "It remains unresolved why Mungyeong told Hyuk Mujin and Gung Gibang that Jin Taekyung ordered them to rescue the Emei Sect.",
    "The nature, purpose, and location-specific significance of the strange formation remain unresolved.",
    "The identity of the person waiting downstairs and avoiding attention remains unclear."
  ],
  "safe_through": 371,
  "temporary_decisions": [
    "Use Satae as the rendering for 사태 and Daoist as the rendering for 도장 in names and forms of address.",
    "Use Cham Isul for 참이슬 and preserve the Korean brand reference with a footnote."
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
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 묘령사태 | **Satae Myo Ryeong** | Middle-aged Emei nun overseeing the funeral prayers. |
| 명진 | **Myeongjin** | Daoist assisting with the funeral rites. |
| 궁기방 | **Gung Gibang** | Young beggar and Future Beggar Chief. |
| 후개 | **Future Beggar Chief** | Title used for Gung Gibang. |
| 기련삼괴 | **Qilian Samgoe** | The trio of monsters that includes Samgoe and Ilgoe. |
| 일괴 | **Ilgoe** | The strongest of the Qilian Samgoe, defeated single-handedly by Jin Taekyung. |
| 칠선자 | **Chilseonja** | Mysterious martial artist who blocked Samgoe's attack and saved Hyuk Mujin. |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 화산신룡 | **Huashan Divine Dragon** | Epithet used for Jin Taekyung. |
| 열화신룡 | **Blazing Fire Divine Dragon** | New epithet acquired by Jin Taekyung. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |
| 천주 | **Heavenly Lord** | Being worshiped as a god by Dark Heaven's fanatics. |
| 혈주 | **Blood Lord** | Dark Heaven figure whose power and abilities are recalled by Jin Taekyung. |
| 열화동 | **Blazing Fire Cave** | Cave at Mount Jiuhua containing an advanced arcane formation. |
| 진성애 | **Jin Seong-ae** | Jin Taekyung's joking title for himself as a sex-education teacher. |
| 구성애 | **Gu Seong-ae** | Real-world sex-education teacher referenced in Jin Taekyung's joke. |
| 삼도천 계곡 | **Valley of the Sanzu River** | Valley named after the Buddhist river separating the living world from the afterlife. |

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
| 혁무진 | 궁기방 | orthodox_ally_to_orthodox_ally | Young Hero Gung | blunt-but-formal | Uses 궁 소협 while teasing Gung Gibang about his injuries. |
| 혁무진 | 청풍 | junior_ally_to_younger_ally | Young Hero Cheong | formal-but-bewildered | Uses 청 소협 when reacting to Cheongpung's warning. |
| 혁무진 | 진태경 | subordinate_to_squad_leader | Squad Leader | deferential | Calls Taekyung 조장님 when announcing his awakening. |
| 궁기방 | 진태경 | squadmate_to_squad_leader | Jin Taekyung | familiar-but-direct | Calls Taekyung by name when he wakes. |
| 진태경 | 청풍고검 | junior_to_elder_sect_leader | Perfected One | respectful-formal | Uses 진인 when greeting the Qingcheng Sect Leader. |
| 청풍고검 | 진태경 | elder_sect_leader_to_junior_ally | Fellow Daoist Jin | respectful-but-familiar | Uses 진 도우 when greeting Taekyung. |
| 멸절신니 | 진태경 | elder_sect_leader_to_benefactor | Benefactor Jin | respectful-formal | Uses 진 시주 when greeting Taekyung. |
| 멸절신니 | 적천강 | orthodox_elder_to_orthodox_elder | Benefactor Jeok | respectful-but-familiar | Uses 시주 when responding to Jeok Cheongang. |
| 진태경 | 적천강 | disciple_to_elder_master | Old Man | casual-but-affectionate | Uses 노야 while thanking Jeok Cheongang. |

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 삼괴 | **Samgoe** | Principal culprit being escorted to Henan |
| 서천마군 | **Western Heaven Demon Lord** | Major obstacle recently overcome by Taekyung |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |

## Listed compact profiles

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 371
- **Aliases:** Slaughter Saint
- **Role:** Young Disciple of the Divine Physician overseeing Jin Taekyung's care
- **Personality:** Regarded as unusually skilled for his age; other traits are not established in this chapter
- **Voice:** Not established in this chapter
- **Relationships:** Disciple of the Divine Physician and physician responsible for Taekyung's recovery

## Korean source

```text
＃372화



“이곳일세.”

“절벽이네요? 평범한.”

다른 사람들과 함께 가파른 절벽 앞에 멈춰선 나는 주위를 둘러봤다.

백여 장에 달하는 높이와 온통 단단한 암석으로 이루어진 절벽의 풍경은 그리 특별해 보일 것도 없었다.

‘여기에 무슨 진법이 있다고?’

하지만 의문이 해결되는 데까지는 그리 오랜 시간이 필요하지 않았다.

문득 느껴지는 기시감을 따라 천천히 걸어간 나는 황갈색의 암벽 앞에서 걸음을 멈췄다.

“이건…….”

모든 것에는 흐름과 결이 있다. 보이지도, 만질 수도 없는 기운이라고 해도 그 범주를 벗어날 수 없다.

그리고 초절정의 경지에 오르며 진일보한 감각은, 부자연스러운 기의 흐름을 감지해 내기에 충분했다.

“진법(陳法)?”

내 중얼거림에 대답하는 목소리가 있었다.

“정확히는 환영진(幻影陳)이다.”

건조한 눈빛으로 내 얼굴을 훑어본 문경, 아니 살성이 앞으로 나서며 손을 뻗었다.

막대한 기의 움직임과 함께 단단하던 암벽이 안개처럼 사라지고 시커먼 동혈의 입구가 모습을 드러낸다.

“아주 개눈깔은 아니로군.”

“어, 예?”

“되묻지 마라.”

한마디를 툭 흘린 살성은 대꾸할 시간도 주지 않고 동혈을 향해 걸음을 옮겼다.

‘저게 욕이야, 칭찬이야.’

이거 묘하게 기분 나쁘네.

그렇다고 막상 화를 내는 것도 뭐한 것이, 살성의 말과 행동에서는 나에 대한 어떤 악감정도 느껴지지 않았다. 그저 다른 사람들을 대하는 것처럼 무미건조한 딱딱함만이 느껴질 뿐이다.

이러니 듣는 사람으로서는 화가 나기보다 머쓱해질 수밖에.

“…….”

물론 상대가 상대인지라 좋게좋게 넘어가려는 것도 있다.

살성이 그렇다는데 뭐 어쩔 거야. 좀 기분 나쁘더라도 참아야지.

몽정 얘기를 꺼내놓고도 멀쩡히 서 있는 것만으로도 감지덕지다.

‘살성을 쌀성으로 만들어 버릴 뻔했는데, 이 정도면 양반이지.’

그런 생각을 하고 있을 때, 옆에서 낮은 웃음소리가 들려왔다. 고개를 돌려보니 입꼬리를 씰룩거리는 적천강이 보였다.

“갑자기 왜 웃으세요?”

“그냥. 살성 저놈도 어지간히 솔직하지 못한 놈이구나, 하는 생각이 들어서.”

“예?”

“되묻지 마라.”

“……?”

뭐지. 최신 유행어인가.

그 말을 끝으로 휘적휘적 걸어가는 적천강의 뒷모습을 바라보던 나와 두 장문인은 시커먼 동혈을 향해 걸음을 내디뎠다.

‘그나저나…….’

이런 곳이 숨겨져 있었다니.

심지어 사천의 중심인 성도에서 한나절이면 올 수 있는 거리다. 평범한 양민의 걸음으로 한나절이니, 무공을 익힌 이들이라면 말할 것도 없다.

나는 끝없이 이어지는 동굴을 걸으며 주위를 둘러봤다.

‘입구부터 엄청 넓네. 사천당문의 지하 뇌옥보다 몇 배는 더.’

오면서 간략히 들었다. 바로 이 동굴에서 암천의 흉수들이 머물렀다고.

그렇게 많은 숫자가 어디에서 튀어나왔나 했더니, 여기에 숨어서 때를 기다리고 있었던 모양이다.

‘그런데 여기까지는 어떻게 들어온 거지?’

서천마군의 지휘 아래, 당문에 쳐들어온 적들의 숫자만 삼백여 명이다.

거기에 더해 청성과 아미로 향한 놈들까지 합친다면 결코 무시할 수 없는 머릿수가 된다.

‘사천성 치안이 그 정도로 개판인가. 아니, 아무리 그래도 개방과 하오문이라면 알아차렸을 것 같은데.’

한 줄기 의문을 품은 채 얼마나 걸었을까.

장정 열 명이 나란히 걸어도 될 만한 넓은 길이 끝나고 마침내 새로운 공간이 모습을 드러냈다.

그 순간, 나도 모르게 혼잣말이 흘러나왔다.

“……허. 이것 봐라.”

족히 천여 명은 수용하고도 남을 것 같은 면적. 천장에 박힌 수십 개의 야명주(夜明珠)가 은은한 빛을 뿌리고, 한구석에는 건량과 벽곡단이 가득 쌓인 항아리와 병장기 등이 놓였다.

그러나 내가 가장 놀란 것은 따로 있었다.

‘저게 뭐야.’

동굴 바닥 전체를 뒤덮고 있는 기이한 문양들.

마치 정교한 톱니바퀴처럼, 일정한 배치로 새겨진 그것들은 마치 오래전 잊힌 고대 왕국의 유적지 같았다.

“혹시 저게 아까 말씀하신 그……?”

내 물음에 청성파의 장문인인 청풍고검이 무거운 얼굴로 고개를 끄덕였다.

“맞네. 저것이 빈도가 말했던 기이한 진법일세.”

설마 했는데, 진짜 진법이었다니.

성라대연에서 진법을 포함한 각종 기관진식을 겪어 본 적이 있었지만 저만큼 크고, 이상한 건 처음 봤다.

‘이 정도면 기이한 걸 넘어서 기형적인데.’

어쩌면 신비로우면서도 위험해 보이는 문양 때문일지도 모른다.

나와 비슷한 생각을 했는지 적천강이 입을 열었다.

“그런데 저 괴상한 문양은 도대체 뭐지?”

“그것이…… 저희 쪽에서도 아직 알아낸 바가 없습니다.”

청풍고검에 이어 멸절신니가 말을 보탰다.

“지금으로서는 속단할 수 없소. 진법의 일부를 본떠 여러 석학과 명사들에게 보여 주었으나 아는 이가 없더구려. 아무도 모르는 서역(西域)의 문자일 가능성도 완전히 배제할 수 없겠소.”

그런데 그때, 나도 모르게 입술 사이로 한마디가 튀어나왔다.

“어, 이거 문자 아닌데?”

“……?”

“……?”

“……?”

모두의 시선이 나를 향해 쏠렸다. 동굴에 들어온 이래 시종일관 침묵을 지키던 살성이 불쑥 입을 열었다.

“근거는?”

“그, 근거요?”

“그렇게 주장하는 데에는 합당한 근거가 있을 터. 되묻지 말고 대답해라.”

당연히 있다. 수만 권의 책을 독파하며 지식을 쌓은 유명한 학자도, 일평생 무림을 종횡하며 수많은 경험을 한 무림의 명사도 반박할 수 없는 확실한 근거가.

‘통합 언어 팩.’

시스템의 힘으로 모든 언어를 자동으로 통역해 주는 [통합 언어 팩].

이것만 있으면 의사소통은 물론이고 글자를 읽고 쓰는 것까지 아무 문제가 없다.

현대에서 스켈레톤 워로드와 대화를 할 수 있었던 이유도 [통합 언어 팩] 덕분이었다.

그러나 패시브 스킬처럼 상시 적용되는 해석 기능에도 진법을 이루는 문양은 처음 모습 그대로였다. 이건 저 문양이 문자가 아니라는 확실한 근거다.

문제는…….

‘이걸 어떻게 설명하냐.’

괜히 말했다. 그냥 가만히 있을걸.

하지만 이미 너무 늦어 버렸다. 점점 깊어지는 살성의 눈빛에, 나는 더듬더듬 입을 열었다.

“찌, 찌.”

“찌찌?”

쌀성의 눈썹이 꿈틀거렸다. 처음으로 보이는 감정 표현. 몽정 사건을 떠올렸음이 분명하다.

“아, 아니, 찌찌가 아니고요.”

“그럼. 젖인가?”

“…….”

제발. 감정이라고는 한 톨도 느껴지지 않는 얼굴로 그런 말 하지 마.

“아니, 그게 아니고요.”

내가 황급히 손을 내젓던 그때, 적천강이 불쑥 끼어들었다.

“지금 내 제자를 겁박하는 건가? 감히 이 화왕의 후인이자 열화문의 소문주를?”

“겁박이라. 할 필요도 없지만 못 할 것도 없지.”

“우연찮게 구명의 은을 입어 참으려고 했는데, 문가(文家), 네놈이 이리 나온다면 노부도 가만히 있을 수 없지.”

점점 험악해지는 분위기 속. 나는 두 눈을 질끈 감으며 외쳤다.

“찌, 찍었는데요!”

“……!”

“……!”

“……!”

“예전에 책에서 본 것 같기도 하고…… 제 느낌상 글자가 아닌 것 같아서, 찍었습니다.”

순간 내려앉은 고요한 침묵. 들릴락 말락 하게 한숨을 내쉰 살성이 적천강에게 물었다.

“그래서, 저놈이 화왕의 후인이자 열화문의 소문주라고?”

잠시 말이 없던 적천강이 대답했다.

“생각해 보니 정식으로 입문식을 치르진 않았군.”

“…….”

“그러니까 엄연히 따지자면 본문의 정식 제자는 아닌 게지. 즉, 아직까지 이 녀석은 태원진가 소속이라고 봐야…….”

나와 시선이 마주친 적천강이 슬그머니 시선을 회피했다.

“여기까지 하겠네.”

“…….”

뭘 여기까지 해. 이미 할 말 다 해 놓고.

스승과 제자 간의 신뢰가 박살 나는 현장을 눈앞에서 목격한 멸절신니와 청풍고검이 떨떠름한 얼굴로 화제를 돌렸다.

“크흠. 어찌 되었건 이 기이한 진법에 관한 문제는 계속해서 알아봐야 할 것 같소.”

“지, 진 도우와 적 선배님의 고견이 큰 도움이 되었습니다.”

하나도 도움이 안 됐다는 건 하늘도 알고 땅도 알고 여기 있는 모두가 안다.

뒷골목 똥개도 안 믿을 소리로 상황을 일단락한 청풍고검이 그늘진 얼굴로 멸절신니에게 말했다.

“그나저나 참으로 믿을 수 없는 일입니다. 고작 진법으로 그 많은 숫자를 불러오다니. 허, 참.”

“그러게 말이오. 이런 일이 가능하다는 건 천하 각지 어디에서도 놈들이 나타날 수 있다는 것 아니겠소?”

잠깐, 지금 뭐라고?

설명하지 못하는 답답함과 찌찌의 후유증에 땅만 쳐다보고 있던 나는 고개를 번쩍 쳐들었다.

“왜 그러시는가, 진 시주?”

“아니. 방금 두 분께서 진법에 관해 나누신 이야기를 저는 처음 듣는 것 같아서요.”

“음? 이동진(移動陳) 말인가?”

“……이동진이요?”

“그렇다네. 삼괴의 말에 의하면 저 기이한 진법은 이동진이라고 불린다더군. 어디까지 믿어야 할지 알 수 없는 허무맹랑한 소리지만…… 암천은 저 진법을 통해 수백 리 거리를 뛰어넘어 이동했다고 하네.”

이동진. 이동진이라니.

갑자기 각진 뿔테 안경을 쓴 평론가가 걸어 나와서 이 진법의 별점은 네 개 반입니다, 라고 해도 지금만큼 당황스럽진 않을 거다.

‘이거, 어디서 많이 듣던 건데.’

거리를 뛰어넘어 수백 명을 이동시키는 진법이라니.

다시 떠올릴수록 가슴이 거세게 뛰고 입술이 바싹 마른다.

만약, 이동진이라 불리는 이 진법이 지금 내가 생각하고 있는 ‘그것’이라면?

‘아니, 그럴 리가.’

그러나 애써 부정하는 속마음과는 달리, 나도 모르게 목울대가 크게 일렁였다.

“혹시, 이 진법. 지금도 가동되는 겁니까?”

두 장문인을 향한 물음이었지만, 대답이 흘러나온 것은 살성의 입이었다.

“삼괴. 놈을 이곳에서 직접 잡았지.”

“……이동진을 통해 도주하려 했군요.”

“그래. 하지만 그건 놈의 생각일 뿐이었다.”

“그 말씀은…….”

“후에 놈이 실토한 대로 진법을 가동하려 했지만, 아무런 일도 일어나지 않았다.”

“아.”

“한 가지는 확실하지. 저 진법에서는 아무런 기의 흐름도 느껴지지 않는다. 이제는 힘을 완전히 상실한 껍데기에 지나지 않아.”

고저 없는 목소리로 설명을 끝마친 살성이 한 마디를 덧붙였다.

“지금까지 드러난 정황을 보건대, 암천은 틀림없는 마교의 후신(後身)이다. 마교가 보유한 괴공절학(怪功絶學)은 셀 수도 없이 많으니 어떤 기이한 술법이 있다고 한들 이상하지 않지.”

마교가 어떤 곳인지는 오래전부터 귀에 못이 박이도록 들어 왔다.

사마외도(邪魔外道) 그 자체라 할 수 있는 강대한 종교 집단.

비록 최종적으로는 정마대전에서 패배했지만, 상당한 기간 천하 무림을 상대로 압도할 수 있었던 것은 마교가 보유한 괴공절학 덕택이었다.

‘그럼 이 진법도 마교로부터 전해진 수많은 괴공절학 중 하나라고?’

생각해 봐도 도저히 모르겠다. 예전에 봤던 퓨전 판타지 소설에서 자주 나오던 소재라 그런가. 괜히 더 헷갈리는 기분이다.

‘묵형에서는 잘만 넘어가던데. 후, 완결도 안 나는 걸 괜히 봐 가지고.’

그래도 혹시 모르니 진법의 배치와 문양 정도는 외워 두기로 했다.

내가 뚫어져라 이동진을 보며 머릿속에 새겨 나가던 그때, 살성이 문득 입을 열었다.

“네 태도를 보아하니 뭔가 아는 것 같은데. 혹 짚이는 것이라도 있느냐?”

“…….”

이건 뭐라고 변명을 해야 하나.
```

## Final English reading copy

```markdown
# Chapter 372

“This is the place.”

“It’s a cliff. A perfectly ordinary one.”

I stopped in front of the steep cliff with the others and looked around.

There was nothing particularly remarkable about it. The cliff rose more than a hundred jang[^1] into the air, and its entire surface was made of solid rock.

*There’s a formation here?*

But it did not take long for my question to be answered.

Following a strange sense of déjà vu, I slowly walked forward and stopped in front of a yellow-brown rock wall.

“This is…”

Everything has a flow and a grain. Even qi, which cannot be seen or touched, cannot escape that principle.

And the senses I had honed by advancing into the Supreme Peak realm were more than enough to detect an unnatural flow of qi.

“A formation?”

A voice answered my mutter.

“More precisely, an Illusion Formation.”

Mungyeong—no, the Slaughter Saint—studied my face with dry eyes, then stepped forward and extended a hand.

With a massive surge of qi, the solid rock wall vanished like mist, revealing the entrance to a pitch-black cavern.

“So your eyes aren’t completely useless after all.”

“Huh?”

“Don’t ask.”

The Slaughter Saint tossed out that one remark, then walked toward the cavern without giving me time to respond.

*Was that an insult or a compliment?*

It left me feeling oddly irritated.

Still, it would have been awkward to get angry when neither the Slaughter Saint’s words nor his actions showed any particular hostility toward me. He was merely as dry and rigid with me as he was with everyone else.

As a result, it was impossible to feel angry. All I could do was feel awkward.

“…”

Of course, the fact that I was trying to let it slide had something to do with who I was dealing with.

If that was how the Slaughter Saint was, what could I do about it? Even if it bothered me, I had to endure it.

The mere fact that I was still standing after bringing up wet dreams was already something to be grateful for.

*I nearly turned the Slaughter Saint into the Spurt Saint. Compared to that, this is downright civilized.*

While I was thinking that, a low chuckle came from beside me. I turned my head and saw Jeok Cheongang’s lips twitching.

“Why are you suddenly laughing?”

“Nothing. I was just thinking that the Slaughter Saint is remarkably bad at being honest about his feelings.”

“Huh?”

“Don’t ask.”

“…”

What was this? Was it some kind of new catchphrase?

After Jeok Cheongang sauntered away, the two Sect Leaders and I walked toward the black cavern.

*More importantly…*

Who would have thought a place like this was hidden here?

It was only half a day’s journey from Chengdu, the heart of Sichuan. That was by the pace of an ordinary commoner, so for martial artists, it would take even less time.

I looked around as I walked through the endless cave.

*The entrance alone is enormous. It’s several times larger than the underground prison beneath the Sichuan Tang Clan.*

I had heard a brief explanation on the way. Dark Heaven’s villains had been staying in this very cavern.

So that was where all those people had come from. They must have been hiding here, waiting for the right moment.

*But how did they get here in the first place?*

Under the command of the Western Heaven Demon Lord, more than three hundred enemies had invaded the Tang Clan alone.

If I added the men who had headed toward Qingcheng and Emei, the number became impossible to ignore.

*Is Sichuan’s security really that terrible? No, even if it was, surely the Beggars’ Sect and the Lower District Sect would have noticed.*

I had been walking with that question in mind for some time when the broad passage—wide enough for ten sturdy men to walk side by side—finally came to an end, and a new space opened before us.

Without meaning to, I muttered,

“…Well, look at this.”

The area was large enough to comfortably accommodate more than a thousand people. Dozens of night-shining pearls embedded in the ceiling cast a soft light, while jars and containers filled with dried provisions and grain-avoiding pills were stacked in one corner alongside weapons and other supplies.

But something else caught my attention far more than any of that.

*What is that?*

Strange patterns covered the entire floor of the cavern.

Engraved in a regular arrangement like elaborate gears, they looked like the ruins of an ancient kingdom forgotten long ago.

“Is that the thing you mentioned earlier…?”

At my question, Clear Wind Ancient Sword, the Sect Leader of the Qingcheng Sect, nodded gravely.

“Yes. That is the strange formation I mentioned.”

I had suspected as much, but it was still astonishing to see that it really was a formation.

I had encountered all kinds of mechanisms and formations at the Star-Netted Grand Banquet, but I had never seen anything so large or so strange.

*At this point, it’s gone beyond strange and become downright malformed.*

Perhaps it was because of the mysterious, dangerous-looking patterns.

Jeok Cheongang seemed to have had the same thought.

“But what in the world are those bizarre patterns?”

“We have not yet determined that ourselves.”

Then Extinction Divine Nun added,

“We cannot jump to conclusions at this point. We copied a portion of the formation and showed it to several renowned scholars and eminent figures, but none of them recognized it. We cannot completely rule out the possibility that it is writing from some unknown region of the Western Territories.”

Then, without meaning to, I blurted out,

“Uh, these aren’t letters.”

“…”

“…”

“…”

Everyone’s eyes turned toward me.

The Slaughter Saint, who had remained silent ever since entering the cavern, suddenly spoke.

“Your basis?”

“M-my basis?”

“If you claim that, you must have a reasonable basis. Answer without asking another question.”

Of course I did. I had a firm basis that neither a renowned scholar who had built up knowledge by reading tens of thousands of books nor an eminent martial artist who had spent a lifetime roaming the Murim and gathering countless experiences could refute.

*The Integrated Language Pack.*

The Integrated Language Pack automatically translated every language through the power of the System.

With it, I could communicate without difficulty, and I could also read and write.

It was thanks to the Integrated Language Pack that I had been able to converse with the Skeleton Warlord in the modern world.

Yet even though its translation function was always active like a passive Skill, the patterns making up the formation remained exactly as they were.

That was conclusive proof that the patterns were not writing.

The problem was…

*How am I supposed to explain that?*

I shouldn’t have said anything. I should have just kept my mouth shut.

But it was already too late. As the Slaughter Saint’s gaze grew more intense, I stammered,

“J-j…”

“Jugs?”

The Spurt Saint’s eyebrow twitched. It was the first emotion I had seen from him. He had clearly remembered the wet-dream incident.

“N-no, not jugs.”

“Then what? Breasts?”

“…”

Please. Don’t say things like that with a face that doesn’t show a single hint of emotion.

“No, that’s not what I meant.”

Just as I frantically waved my hands, Jeok Cheongang suddenly cut in.

“Are you threatening my disciple? How dare you threaten the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

“Threatening him? There is no need for that. But it is not beyond my ability.”

“I was trying to hold back because I owe you my life, but if you, Wen, are going to act like this, this old man cannot sit back and do nothing.”

The atmosphere grew increasingly hostile.

I squeezed my eyes shut and shouted,

“I—I guessed!”

“…”

“…”

“…”

“I think I saw it in a book once… It just felt like it wasn’t writing, so I took a guess.”

A deep silence descended.

The Slaughter Saint let out a nearly inaudible sigh, then asked Jeok Cheongang,

“So that man is the Fire King’s heir and the Young Sect Leader of the Fire Gate Clan?”

Jeok Cheongang was silent for a moment before answering.

“Now that I think about it, he never went through a formal initiation ceremony.”

“…”

“So, strictly speaking, he isn’t an official disciple of our sect. That means he still belongs to the Jin Family of Taiyuan—”

Jeok Cheongang’s eyes met mine. He quietly looked away.

“We’ll stop here.”

“…”

What did he mean, stop here? He had already said everything there was to say.

Extinction Divine Nun and Clear Wind Ancient Sword, who had just witnessed the trust between master and disciple being utterly destroyed, awkwardly changed the subject.

“Ahem. In any case, it seems we will have to continue investigating this strange formation.”

“Y-yes. Fellow Daoist Jin and Senior Jeok’s insights were a great help.”

Everyone here, along with heaven and earth, knew that they had not helped at all.

Even a stray dog in a back alley would not have believed that, but Clear Wind Ancient Sword used it to bring the situation to an end before speaking to Extinction Divine Nun with a troubled expression.

“More importantly, this is truly unbelievable. To bring that many people here with nothing but a formation… My goodness.”

“Indeed. If such a thing is possible, does that not mean they could appear anywhere across the land?”

Wait. What did he just say?

I had been staring at the ground, frustrated by my inability to explain myself and still suffering the aftereffects of the boob incident. I suddenly jerked my head up.

“What’s the matter, Benefactor Jin?”

“No. I think this is the first time I’ve heard what you two just said about the formation.”

“Hm? You mean the Transportation Formation?”

“…The Transportation Formation?”

“That is what Samgoe called it. According to him, that strange formation is a Transportation Formation. It is an absurd claim, and we have no way of knowing how much of it to believe, but he said Dark Heaven used it to cross hundreds of li.”

A Transportation Formation. He said a Transportation Formation.

Even if a critic wearing angular horn-rimmed glasses had suddenly walked over and said, “I give this formation four and a half stars,” I would not have been any more bewildered than I was now.

*This sounds familiar.*

A formation capable of moving hundreds of people across hundreds of li.

The more I thought about it, the harder my heart pounded and the drier my lips became.

*What if this formation called the Transportation Formation was that thing I was thinking of?*

*No. That couldn’t be.*

But despite my desperate attempts to deny it, my throat bobbed heavily.

“Is this formation still operational?”

I had directed the question at the two Sect Leaders, but the answer came from the Slaughter Saint.

“Samgoe. I caught him here myself.”

“…He tried to escape through the Transportation Formation.”

“Yes. But that was only what he intended to do.”

“What do you mean?”

“As he later confessed, he tried to activate the formation. Nothing happened.”

“Ah.”

“One thing is certain. There is no flow of qi coming from that formation. It has completely lost its power. Now it is nothing more than an empty shell.”

After explaining that in his level voice, the Slaughter Saint added,

“Judging by the circumstances revealed so far, Dark Heaven is unquestionably a successor of the Demonic Cult. The Demonic Cult possesses countless bizarre and supreme arts. It would not be strange for them to have any number of strange techniques.”

I had heard what kind of place the Demonic Cult was so many times that the words had practically been hammered into my ears.

A powerful religious organization that was the very embodiment of evil, demonic, and heretical ways.

Although it had ultimately lost the Great Faction War, the Demonic Cult had been able to overwhelm the Murim for a considerable period thanks to its bizarre and supreme arts.

*Then this formation is one of the countless strange arts passed down from the Demonic Cult?*

No matter how much I thought about it, I could not figure it out. Maybe it was because this was such a common device in the fusion-fantasy novels I had read before. It only made me more confused.

*It worked just fine in Muk-hyeong.[^2] Sigh. I shouldn’t have bothered reading something that never even got an ending.*

Still, just in case, I decided to memorize the formation’s layout and patterns.

As I stared intently at the Transportation Formation and carved every detail into my memory, the Slaughter Saint suddenly spoke.

“Judging by your attitude, you seem to know something. Does anything come to mind?”

“…”

What excuse was I supposed to make now?

[^1]: A *jang* is a traditional East Asian unit of length, roughly ten feet.

[^2]: *Muk-hyeong* is the title of a fusion-fantasy novel Jin Taekyung has read.
```
