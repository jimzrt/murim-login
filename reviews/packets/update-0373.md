<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0373.txt",
      "sha256": "f7e7fcb5c21526b3fcf30d133884442261cacbe38e3e8eb9256bbd37c0fd334d",
      "bytes": 14543
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a54ae647e222876646a55a65a35202cd5dc355ed97ac8ed4b9073fcf9ba6da5e",
      "bytes": 938
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "555a8e90504fbbf7fae8708b05289615b30c1e083db0bd562dade2aea4fe96db",
      "bytes": 5567
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "841cdb2cecfd823d69afaf961829a601d6c896e307d537986212c869aba893ae",
      "bytes": 5011
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "5b42cf27069da9e42d18c3444e21cbcc13c9810cb9f795b7b1c55e529f101b23",
      "bytes": 511
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6f3f8194f28f6e29a32fbcfd60263ef7d66f18215d373bd42dd94b116a96ce38",
      "bytes": 3481
    },
    {
      "path": "docs/EXPEDITION_SEED.md",
      "sha256": "e5a01d50d796fba043e2eff7ee06ea15a89df4e1c84e4ef61e52603f1ccb41b3",
      "bytes": 1897
    }
  ],
  "estimated_tokens": 11902
}
-->

# Durable State Update — Chapter 373

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 373. Keep at most
2 continuity_sources. Use only chapter
numbers through 373. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.

Return this exact shape:

{
  "chapter": 373,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 373,
    "continuity_sources": [373],
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
    "A hidden cavern near Chengdu concealed Dark Heaven forces and contained supplies, weapons, and a vast unidentified formation.",
    "The formation called 이동진 by Samgoe was used to transport hundreds of people across hundreds of li, but it has completely lost its power and cannot currently be activated.",
    "Taekyung can determine through the Integrated Language Pack that the formation's patterns are not writing, but he cannot explain how he knows."
  ],
  "continuity_sources": [
    372
  ],
  "open_questions": [
    "What was the original purpose and mechanism of the Transportation Formation?",
    "What does Taekyung suspect the formation is, and how did he recognize it?"
  ],
  "safe_through": 372,
  "temporary_decisions": [
    "Use Transportation Formation for 이동진.",
    "Preserve Spurt Saint as the translation of the 쌀성 wordplay in this exchange."
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
| 적천강 | 문경 | orthodox_elder_to_younger_orthodox_elder | Wen | hostile-but-blunt | Jeok Cheongang addresses Mungyeong as 문가 while intervening on Taekyung's behalf. |

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 아이템              | **Item**                       |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 문경 | **Mungyeong** | Young Disciple of the Divine Physician overseeing Jin Taekyung's care. |
| 사천당문 | **Sichuan Tang Clan** | The Tang family and clan of Sichuan |
| 신의 | **Divine Physician** | Honorific for the physician treating Tang Sadok. |
| 백염 | **White Flame** | Previously bound item listed by the System. |
| 아미파 | **Emei Sect** | Orthodox sect whose nuns conduct the funeral rites. |
| 청성파 | **Qingcheng Sect** | Orthodox sect represented among the assisting martial artists. |
| 개방 | **Beggars' Sect** | Organization represented by the attending beggars. |
| 후개 | **Future Beggar Chief** | Title used for Gung Gibang. |
| 청풍고검 | **Clear Wind Ancient Sword** | Sect Leader of the Qingcheng Sect; epithet of the old Daoist. |
| 멸절신니 | **Extinction Divine Nun** | New Sect Leader of the Emei Sect after the death of the Heaven-Shaking Divine Nun. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 371
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 372
- **Aliases:** Slaughter Saint
- **Role:** Young Disciple of the Divine Physician overseeing Jin Taekyung's care
- **Personality:** Regarded as unusually skilled for his age; dry, rigid, emotionally restrained, and blunt in his interactions
- **Voice:** Not established in this chapter
- **Relationships:** Disciple of the Divine Physician and physician responsible for Taekyung's recovery

## Korean source

```text
＃373화



돌아오는 길은 짧았다.

가는 길에는 정황을 주고받느라 속도라도 조절했지, 게임으로 치자면 초절정 고수가 자그마치 다섯이나 함께하는 초호화 파티다.

평범한 사람이었다면 한나절이 걸렸을 거리는 이제 바짝 좁혀져 있었다.

“수고했네, 진 시주.”

“아직 피로할 터인데 따라와 줘서 고맙고.”

사천당문 인근에 이르러 인사를 건네는 두 장문인의 말에 나는 어깨를 으쓱해 보였다.

“아닙니다. 별로 도와드린 것도 없는데요, 뭐.”

“하긴.”

“그건 그렇지.”

“…….”

아니, 도움이 못 된 건 사실이긴 한데 이건 너무한 거 아니냐.

나를 보며 희미하게 웃어 보인 청풍고검이 살성과 적천강을 향해 포권을 취했다.

“두 분 선배님들께도 감사드립니다. 괜한 발걸음을 하게 만든 것이 아닌가 싶어 송구스럽군요.”

살성과 적천강이 동시에 대답했다.

“괜한 발걸음은 맞았지.”

“다음부터는 송구스러워할 일을 만들지 말게. 알았나?”

“……아, 예.”

그래, 내가 딱 저 기분이었다니까.

떨떠름한 표정의 청풍고검을 향해 살성이 말을 이었다.

“그리고…… 앞으로는 나를 찾는 일이 없길 바라지.”

귀찮으니 적당히 불러라, 라는 뜻이 아니다. 잠시 살성으로 돌아왔던 그는 다시 어린 의생, 문경으로 돌아가려 하고 있었다.

나는 물론이고 이 자리의 모두가 그 말에 담긴 의미를 알아차렸다.

그중에서도 가장 당황한 것은 두 장문인이었다.

“서, 선배. 그건…….”

“시주. 다시 한번 생각해 봄이 어떻겠소?”

그러나 대답 대신 돌아온 것은 살성의 건조한 눈빛이었다.

잠시 말이 없던 청풍고검과 멸절신니가 작은 한숨과 함께 고개를 끄덕였다.

“……그리하겠습니다.”

“시주의 뜻을 존중하리다. 지금 당장은.”

지금 당장은. 마지막에 덧붙인 말에 유난히도 힘이 실려 있다. 살성의 입술 사이로 나직한 목소리가 흘러나왔다.

“이번에 나선 것은 자그마한 변덕이었을 뿐, 내 뜻은 바뀌지 않는다.”

일말의 여지조차 주지 않는 단호한 대답. 살성의 눈동자가 나와 적천강을 향했다.

“두 사람도 알아들었으리라 믿지.”

적천강이 불쑥 입을 열었다.

“다시 어울리지도 않는 의생 행세를 할 셈인가?”

“행세가 아니야. 살성은 이미 존재하지 않고, 한 사람의 의생만이 남았다.”

“호랑이가 염소 가죽을 뒤집어쓴다 한들, 그것을 염소라고 부를 수 있을까.”

“이빨을 감추고 발톱을 숨긴다면 호랑이도 염소가 될 수 있지.”

“하지만 결국 마지막 순간 발톱을 드러냈고. 안 그런가?”

살성의 미간에 얕은 골이 파였다.

“나이가 들더니 말이 더 많아졌군. 내게 빚진 것이 있을 텐데.”

“……거참. 틀린 말이 아니라 뭐라 말도 못 하겠군.”

“대답한 것으로 알지.”

적천강과의 대화를 일축한 살성이 나를 힐끗 바라봤다.

“넌?”

“저요?”

“그럼 남은 게 또 누가 있느냐?”

“아뇨, 그게 아니라. 저한테 선택권이 있는 겁니까?”

“물론. 두 가지 선택지가 있다.”

살성이 무뚝뚝한 표정으로 입을 열었다.

“첫째. 문경이라는 어린 의생의 정체가 살성이라는 걸 떠벌린 다음 쥐도 새도 모르게 변사체로 발견되는 것. 그리고 두 번째. 아무도 눈치채지 못하게 입을 다물고 전처럼 나를 대하다가 조용히 떠나는 것.”

“…….”

“어느 것으로 하겠나?”

이야, 너무 어려운 선택지라서 순간 할 말을 잃었다.

마른침을 꿀꺽 삼킨 내가 입을 열었다.

“두 번째로.”

“잘 생각했다.”

“응.”

내 신속한 대답에 고개를 끄덕이려던 살성이 멈칫했다.

“지금, 뭐라고?”

“왜?”

“뭐?”

“아니, 왜 그래. 전처럼 편하게 대하라면서.”

“……!”

“……!”

두 장문인은 입을 딱 벌렸고, 잠시 말을 잇지 못하던 살성은 낄낄 웃고 있는 적천강을 향해 물었다.

“이거, 미친놈인가?”

“원래 그런 놈이다. 어때, 골 때리지?”

“골을 부수고 싶은데.”

나는 골이 부서지기 전에 넙죽 고개를 숙였다.

“아, 제가 순간적으로 착각을 해서 그만. 죄송합니다.”

“……개도 안 믿을 소리지만, 이번 한 번은 넘어가 주지.”

실수인 척 한번 엿 먹이려는 게 너무 티가 났나. 잠깐 가늘어진 눈동자로 나를 노려보던 살성이 입을 열었다.

“어쨌건 앞으로는 유의해라. 이 자리에 있는 사람들을 제외하면 나에 관한 사실은 아무도 모르니. 아, 청풍 그 아이는 예외다. 내 제자는 당연하고.”

“청 소협도 알고 있었습니까?”

“그래. 그 아이를 제외하고 그날 내 모습을 본 놈들은 모두 죽었다.”

사후처리 깔끔한 것 보소. 왜 사천당문에는 포로가 한 놈도 없었는지 이제야 이해가 간다.

복면 살성. 가면을 벗으면 패널이고 방청객이고 싹 다 뒈지는 거다.

‘그나저나 볼수록 기분 묘하네. 문경이 바로 그 살성이었다니.’

장강에서의 첫 만남 때부터 지금까지의 기억이 휙휙 스쳐 지나갔다.

그가 보여 준 모습 중 무엇이 진실이고 거짓일까.

내가 알던 천진난만하던 어린 의생은 이미 존재하지 않는다. 그저 무미건조한 눈빛을 지닌 천하제일의 살수가 있을 뿐이다.

순간 나도 모르게 한 가지 물음이 입 밖으로 튀어나왔다.

“왜 그토록 스스로를 감추려고 하십니까?”

저 멀리 보이기 시작하는 사천당문을 향해 나아가던 살성의 신형이 갑작스러운 물음에 우뚝 멈췄다.

짧은 침묵 끝에 의외로 차분한 대답이 들려왔다.

“무림이라면 지긋지긋하니까.”

“그래서 떠나신 겁니까?”

“그래. 두 번 다시는 살생을 저지르지 않겠다고 하늘에 맹세했지.”

이곳, 무림에서 살수는 멸시받는 존재다. 정파는 물론이고 사마외도(邪魔外道)에서도 그들은 환영받지 못한다.

더 높은 무학의 경지를 추구하는 무인이 아닌, 오직 살인을 위해 태어난 자들이라고 여겨지기 때문이다.

한 사람의 살수가 살성(殺星)이라는 별호를 얻기까지 얼마나 많은 피를 흘리고 묻혔을까. 그의 마음을 어느 정도 알 것 같았다.

하지만…….

“한편으로는 좀 궁금하네요.”

“뭐?”

“그렇게 싫어하는 무림으로 다시 돌아오신 이유가.”

“……다시 돌아오다니 무슨 헛소리냐.”

살성의 눈동자가 깊게 가라앉았다.

“어쩔 수 없는, 불가피한 선택이었다.”

“글쎄요. 그렇게 말씀하신다면 제가 할 말은 없지만 적어도 몇 가지 선택은 직접 내리신 것 같은데요. 예를 들면……”

나는 뒤통수를 긁적이며 말을 이었다.

“장강에서 마주친 어느 무림인들에게 가는 길이 같다며 동행을 청한다든지, 며칠 후 우연처럼 다시 만나 스리슬쩍 자신의 정체를 알려 준다든지. 그것도 아니면 제 이름을 빌려 개방의 후개에게 아미파를 구원하라 시키고 본인은 청성파로 가서…….”

“그만.”

“예. 안 그래도 그럴 생각이었습니다. 하나하나 말해 보니까 꽤 많네요.”

“무슨 말이 듣고 싶은 것이냐? 그 자리에서 모든 걸 방관한 채, 너와 네 스승을 포함한 수많은 사람이 죽어 가는 것을 지켜보아야 했다는 말이냐?”

“그럴 리가요. 정말 감사드리고 있습니다. 대협.”

비꼬는 것이 아닌, 정말 순도 백 퍼센트의 진심이다. 적절한 때에 나서 준 그가 아니었다면 무수한 사람들이 죽고 다쳤을 테니까.

물론 나와 적천강도 예외는 아니었을 것이다.

그러나 내 대답을 들은 살성의 반응은 사막의 모래알처럼 퍼석했다.

“날 대협이라고 부르지 마라.”

“그럼 뭐라고 부를까요?”

말없이 나를 응시하던 살성이 고개를 돌렸다.

그가 커다란 점처럼 보이는 사천당문을 향해 한 걸음을 떼자 신형이 유령처럼 미끄러진다.

불어오는 바람 사이로 소년의 목소리가 흩어졌다.

“문경. 그것으로 족하다.”

정말 그것으로 족할까. 정답은 오직 그만이 알고 있을 것이다.

나는 어깨를 으쓱하며 대답했다.

“그래, 알았다. 문경아.”

“……!”

그 순간, 앞서나가던 한 사람의 신형이 비틀거렸다.



* * *



전각으로 돌아온 내 뒤로 거머리 두 마리가 따라붙었다.

한 놈은 오른팔인지 새끼손가락인지 헷갈리는 혁무진이고, 다른 하나는 요새 때라도 밀었는지 조금이나마 피부가 하얘진 거지다.

“문경이, 쟤 왜 저래요? 왠지 모르게 조금 어두워진 느낌인데.”

“그럴 수도 있지. 스승인 신의께서도 상처를 입으셨고, 지금 기다리는 환자들도 워낙 많으니.”

“아, 그렇구나. 그런데 조장님, 문경이랑 어디 다녀오셨습니까?”

“애가 울적해 보이니까 바람 좀 쐬게 해 준 거 아냐. 넌 왜 그렇게 멍청하냐?”

“허, 살다 살다 거지한테까지 이런 소릴 들어 보네. 제가 이래 보여도 서책만 몇백 권을 읽은 사람이에요. 어디 가서 멍청하다 소리는 들어 본 적 없습니다.”

아니, 내가 볼 때는 그냥 둘 다 멍청한 것 같은데.

나는 혀끝에 맴도는 살성이라는 두 글자를 꿀꺽 삼켰다. 아마 저 녀석들은 죽었다 깨어나도 모를 거다. 문경의 진짜 정체를.

‘하긴. 그 정도 연기력이면 누구나 속아 넘어가지.’

사람들의 이목이 닿기가 무섭게 살성은 문경으로 돌아갔다.

평소 쾌활했던 소년 의생의 분위기가 아주 조금 어두워졌다고 해서 정체를 의심하는 사람은 아무도 없었다.

아니, 짐작조차 할 수 없었다고 해야 맞겠다.

“사서삼경이면 인정하는데, 끽해야 무협 소설만 줄창 읽어 놓고 서책은 무슨.”

“연애 소설도 읽었습니다. 귀염미(貴艶美) 모르세요?”

“잠깐. 귀염미라면 혹시 후기지수의 유혹, 그놈은 강했다 등등을 쓴 서생?”

“어, 아시네.”

“당연히 알지. 일결 제자 때 구걸한 돈으로 그거 빌려 보다가 왕초한테 먼지 나게 얻어맞았는데. 하, 그 새끼 지금 만나면 타구봉법으로 확 그냥.”

빠박!

“억!”

“악!

사이좋게 추억을 공유하는 두 놈의 엉덩이를 걷어차 내쫓고는 문을 쾅 닫아 버렸다.

저 자식들은 가뜩이나 생각할 일도 많은데 왜 여기 와서 난리인지 모르겠다.

‘이제야 좀 조용해졌네.’

지금쯤이면 청풍은 여기저기 쏘다니고 있을 거고, 적천강도 오늘 하루는 푹 쉬라고 했으니 당분간 날 찾을 사람은 없다.

푹신한 침상에 몸을 눕힌 나는 잠시 미뤄 두었던 일을 하기로 마음먹었다.

‘안 읽은 메시지 확인.’

띠링. 띠링. 띠링, 띠링!

끊임없이 울려 퍼지는 종소리와 함께 허공을 가득 메우는 시스템 창. 예전에도 몇 번 있었던 일이긴 하지만 이 정도면 최고 기록 경신이다.

순간 할 말을 잃은 나는 주요 메시지부터 하나씩 확인해 나갔다.



- [초절정]의 경지에 도달했습니다!

- [Lv.170 노군백]을 처치했습니다!

- 퀘스트, [초대받지 않은 손님]을 성공적으로 완료했습니다!

- 막대한 경험치와 명성을 획득하셨습니다!

- 시스템 메시지가 한도를 초과했습니다. 획득한 경험치와 명성을 합산합니다.

- [Lv.120]에 도달했습니다!

- 명성이 기준치를 돌파함으로써 새로운 별호를 획득합니다!

- 당신은 생사를 오가는 전투 속에서 스스로 깨달음을 얻었습니다. 모든 무공의 경지가 크게 상승하며 새로운 무공을 사용할 수 있습니다!

- [열화신공]의 경지가 팔 성에 도달했습니다!

- [화염신장]의 경지가…….

- [화룡신창]의…….



무수한 악수의 요청, 이 아니라 메시지의 향연.

대충 훑어보는 것만으로도 눈알이 빙글빙글 돌았다.

“……와, 씨.”

이게 다 뭐냐.

아직도 안 읽은 메시지가 절반이나 된다는 사실에 당황스러울 지경이다.

남은 개수를 파악하기 위해 손으로 스크롤을 내리는 그때, 특이한 무언가가 눈에 띄었다.



- 새로운 아이템이 당신에게 종속됩니다.

- 현재 보유 중인 종속 아이템 : [백염], [???]

- 아직 이름이 정해지지 않았습니다. 새로운 이름을 부여하면 아이템은 오롯이 당신에게 종속되며, 어디에서나 인벤토리를 통해 소환할 수 있습니다.



“여기서 이게 뜨네…….”

현대와 무림의 인벤토리는 각각 분리되어 있다. 하지만 백염과 같은 종속 아이템은 공간에 구애받지 않고 어디서든 꺼내 쓸 수 있다.

안 그래도 백염만으로는 아쉬웠던 참이었는데, 이런 행운이라니.

‘주면 나야 땡큐지.’

기대감에 부풀어 인벤토리를 확인하려던 바로 그 순간이었다.

똑똑똑.

문을 두드리는 노크 소리와 함께 한 사람이 빼꼼 고개를 내민다.

“조장님. 저 무진인데요…….”

“꺼져.”

“아니, 그게 아니라요.”

“형 바쁘다. 가서 귀염미 소설이나 봐.”

“어, 조장님도 보셨어요?”

“……아니 이 새끼가 진짜.”

안 되겠다. 우선 아이템 까기 전에 저 자식부터 까야겠다.

내가 침상에서 벌떡 몸을 일으키자 혁무진이 황급히 외쳤다.

“하남! 하남이요!”

“뭐?”

“하남에서 조사단이 왔습니다! 조장님을 찾고 있어요.”

“……조사단?”

앞뒤 다 자른 혁무진의 말에 눈살이 찌푸려진 그때.

띠링.

익숙한 알림이 귓가에 닿았다.
```

## Final English reading copy

```markdown
# Chapter 373

The return trip was short.

On the way there, we had at least adjusted our speed while exchanging information. But if you put it in game terms, this was a lavish party with no fewer than five Supreme Peak masters traveling together.

A distance that would have taken an ordinary person half a day had been reduced to almost nothing.

“You have worked hard, Benefactor Jin.”

“You must still be tired, so thank you for coming with us.”

When the two Sect Leaders spoke to me as we approached the Sichuan Tang Clan, I shrugged.

“It’s nothing. I didn’t really help much, anyway.”

“That’s true.”

“It is.”

“…”

I mean, it was true that I hadn’t helped much, but wasn’t this a little harsh?

Clear Wind Ancient Sword gave me a faint smile, then made a fist-and-palm salute toward the Slaughter Saint and Jeok Cheongang.

“I am also grateful to you two Seniors. I’m sorry that our matter caused you to make an unnecessary journey.”

The Slaughter Saint and Jeok Cheongang answered at the same time.

“It was an unnecessary journey.”

“Don’t give us cause to feel sorry next time. Understood?”

“…”

That was exactly how I felt.

The Slaughter Saint continued, turning toward Clear Wind Ancient Sword.

“And… I hope you never seek me out again.”

He wasn’t saying, *Call me only when it’s convenient because I’m annoyed.* The man who had briefly returned to being the Slaughter Saint was trying to become Mungyeong, the young physician, once more.

Everyone present understood the meaning behind his words.

The two Sect Leaders were the most flustered of all.

“S-Senior, that…”

“Benefactor, perhaps you should reconsider?”

But the only answer they received was the Slaughter Saint’s dry gaze.

After a brief silence, Clear Wind Ancient Sword and Extinction Divine Nun nodded with small sighs.

“…”

“We shall do so.”

“I will respect your wishes, Benefactor. For now.”

The final words—*for now*—were given unusual emphasis. A quiet voice slipped between the Slaughter Saint’s lips.

“My appearance this time was nothing more than a minor whim. My intentions have not changed.”

It was a firm answer that left not even the slightest opening. The Slaughter Saint’s eyes turned toward me and Jeok Cheongang.

“I trust you two understood as well.”

Jeok Cheongang abruptly opened his mouth.

“Are you planning to pretend to be that ill-suited physician again?”

“It isn’t an act. The Slaughter Saint no longer exists. Only one physician remains.”

“Even if a tiger wraps itself in a goat’s hide, can you call it a goat?”

“If it hides its teeth and claws, even a tiger can become a goat.”

“But you revealed your claws in the end. Didn’t you?”

A shallow furrow formed between the Slaughter Saint’s brows.

“You’ve become more talkative with age. You still owe me a debt, you know.”

“…”

“Damn. Since you’re not wrong, I can’t even argue.”

“I’ll take that as your answer.”

After cutting off the conversation with Jeok Cheongang, the Slaughter Saint glanced at me.

“And you?”

“Me?”

“Who else is left?”

“No, that’s not what I meant. Do I have a choice?”

“Of course. You have two choices.”

The Slaughter Saint spoke with an impassive expression.

“First, you can blab that the young physician named Mungyeong is actually the Slaughter Saint, then be found dead somewhere without anyone knowing how it happened. Second, you can keep your mouth shut so no one notices, treat me as you did before, and then leave quietly.”

“…”

“Which will you choose?”

Wow. The choices were so difficult that I was momentarily rendered speechless.

After swallowing hard, I opened my mouth.

“The second one.”

“Good choice.”

“Yeah.”

The Slaughter Saint, who had been about to nod at my quick answer, suddenly stopped.

“What did you just say?”

“Why?”

“What?”

“No, what’s wrong? You said I should treat you comfortably like before.”

“!”

“!”

The two Sect Leaders stood there with their mouths hanging open. The Slaughter Saint, who had been silent for a moment, asked Jeok Cheongang, who was snickering.

“Is this man insane?”

“He’s always been like that. He drives you crazy, doesn’t he?”

“I want to smash his skull.”

I quickly bowed before my skull could be smashed.

“Ah, I was momentarily confused. I apologize.”

“It’s something not even a dog would believe, but I’ll let it go this once.”

*Was it that obvious that I was trying to mess with him under cover of a mistake?*

The Slaughter Saint glared at me with narrowed eyes for a moment before speaking again.

“In any case, be careful from now on. Other than the people present here, no one knows anything about me. Ah, that boy Cheongpung is an exception. My Disciple naturally knows as well.”

“Young Hero Cheong knew too?”

“Yes. Other than that child, everyone who saw me that day is dead.”

*Talk about a clean cleanup.*

Only now did I understand why there hadn’t been a single prisoner at the Sichuan Tang Clan.

*The masked Slaughter Saint. Once the mask comes off, every last panelist and audience member fucking dies.*

*Come to think of it, the more I look at him, the stranger it feels. Mungyeong was the Slaughter Saint all along.*

Memories from our first meeting on the Yangtze until now flashed through my mind.

Which of the appearances he had shown me were true, and which were false?

The innocent young physician I had known no longer existed. Only the greatest assassin in the world remained, with a dry, emotionless gaze.

Before I knew it, a question had burst from my lips.

“Why do you try so hard to hide yourself?”

The Slaughter Saint’s form, which had been moving toward the Sichuan Tang Clan now visible in the distance, suddenly came to a halt.

After a brief silence, an unexpectedly calm answer reached me.

“Because I’m sick to death of the Murim.”

“That’s why you left?”

“Yes. I swore to the heavens that I would never take another life again.”

In this place—the Murim—assassins were despised. They were not welcomed by the orthodox factions, nor by the heterodox and demonic paths.

They were regarded not as martial artists pursuing higher realms of martial arts, but as people born solely to kill.

How much blood had a single assassin spilled and waded through to earn the epithet of Slaughter Saint? I thought I understood his feelings, at least somewhat.

But…

“On the other hand, I’m curious about something.”

“What?”

“Why you came back to the Murim you hate so much.”

“Came back? What nonsense are you talking about?”

The Slaughter Saint’s eyes sank deeply.

“It was a choice I couldn’t avoid. An inevitable one.”

“Perhaps. If that’s how you put it, I have nothing to say. But it seems like you made at least a few choices yourself. For example…”

I scratched the back of my head and continued.

“You asked to travel with some martial artists you met on the Yangtze because you were going the same way. Then, a few days later, you met us again as if by coincidence and subtly revealed your identity. Or you borrowed my name and told the Future Beggar Chief of the Beggars’ Sect to save the Emei Sect, while you went to the Qingcheng Sect and…”

“Enough.”

“Yes. I was about to stop anyway. When I list them one by one, there are quite a lot.”

“What is it you want to hear? That I should have stood by and watched countless people—including you and your master—die?”

“Of course not. I’m truly grateful to you, Great Hero.”

It wasn’t sarcasm. It was one hundred percent sincere.

If he hadn’t stepped in at the right moment, countless people would have been killed or injured.

Jeok Cheongang and I would have been no exception.

But the Slaughter Saint’s response was as dry as grains of sand in a desert.

“Don’t call me Great Hero.”

“Then what should I call you?”

The Slaughter Saint stared at me without a word, then turned away.

As he took a step toward the Sichuan Tang Clan, which looked like a large dot in the distance, his form glided forward like a ghost.

The boy’s voice scattered through the passing wind.

“Mungyeong. That is enough.”

*Would it really be enough?*

Only he knew the answer.

I shrugged and answered.

“Yeah, got it, Mungyeong.”

“…”

At that moment, the figure of the person walking ahead of us staggered.

* * *

Two leeches followed me back to the pavilion.

One was Hyuk Mujin, clinging so close I couldn’t tell whether he was my right arm or my little finger. The other was the beggar, whose skin had become at least a little whiter, as if he had scrubbed himself recently.

“Mungyeong… What’s wrong with him? He seems a little gloomier somehow.”

“That can happen. His master, the Divine Physician, was injured too, and there are so many patients waiting for him.”

“Oh, I see. But, Captain, where did you go with Mungyeong?”

“The kid looked depressed, so Captain must’ve taken him out for some fresh air. Why are you such an idiot?”

“Ha. Never in my life did I think I’d hear something like that from a beggar. I may look like this, but I’ve read hundreds of books. I’ve never been called stupid anywhere.”

*As far as I could tell, both of them were idiots.*

I swallowed the two words *Slaughter Saint* that had been hovering on the tip of my tongue.

Those two would never know Mungyeong’s true identity, even if they died and came back to life.

*Well, with acting skills that good, anyone would be fooled.*

The moment anyone’s attention fell on him, the Slaughter Saint returned to being Mungyeong.

No one suspected him just because the usually cheerful young physician seemed a little gloomier.

No—they couldn’t even have guessed.

“I’d give you credit if it were the Four Books and Three Classics, but you’ve done nothing but read martial-arts novels nonstop. What books are you talking about?”

“I’ve read romance novels too. Don’t you know Gwiyeommi?[^1]”

“Wait. If it’s Gwiyeommi, are you talking about the scholar who wrote *The Seduction of a Young Prodigy*, *That Guy Was Strong*, and so on?”

“Hey, you know him.”

“Of course I do. When I was a First-Knot Disciple, I used money I’d begged for to rent one of those books, and the boss beat the dust out of me. Ha. If I ever meet that bastard again, I’ll use the Dog-Beating Staff Technique to—”

*Whack!*

“Gah!”

“Ow!”

I kicked the two of them in the butt and sent them packing, then slammed the door shut.

I didn’t know why those idiots had come here to make such a racket when I already had more than enough to think about.

*At last, some quiet.*

Cheongpung was probably running around all over the place by now, and Jeok Cheongang had told me to take the day off and get some proper rest. No one would be looking for me for a while.

I lay down on the soft bed and decided to take care of something I had put off for a while.

*Check unread messages.*

*Ding. Ding. Ding, ding!*

Chimes rang out without end as System windows filled the air. This had happened a few times before, but this was a new record.

Momentarily speechless, I began checking the important messages one by one.

> **System**
>
> - You have reached the **Supreme Peak** realm!
> - You defeated **Lv. 170 No Gunbaek**!
> - Quest **Uninvited Guest** completed successfully!
> - You have acquired a massive amount of **EXP** and **Fame**!
> - The System message limit has been exceeded. Acquired **EXP** and **Fame** will be totaled.
> - You have reached **Lv. 120**!
> - Your **Fame** has surpassed the threshold. You have acquired a new **Title**!
> - You gained enlightenment on your own in battles where life and death hung in the balance. All your martial arts have advanced significantly, and you can now use new martial arts!
> - The realm of **Blazing Flame Divine Technique** has reached the **Eighth Stage**!
> - The realm of **Flame Divine Palm** has…
> - The realm of **Fire Dragon Divine Spear**…

Countless requests for handshakes—no, a feast of messages.

Just skimming through them made my eyes spin.

“…Whoa, shit.”

What was all this?

I was nearly thrown into a panic when I realized that half of the unread messages still remained.

As I scrolled down with my hand to figure out how many were left, something unusual caught my eye.

> **System**
>
> - A new **Item** is now bound to you.
> - Currently bound **Items:** **White Flame**, **???**
> - No name has been assigned yet. If you give it a new name, the Item will become completely bound to you and can be summoned through your Inventory from anywhere.

“This pops up here…”

The modern-world Inventory and the Murim Inventory were separate.

However, bound Items like White Flame could be taken out anywhere, unaffected by space.

I had already been feeling that White Flame alone wasn’t quite enough, so this was incredible luck.

*If you’re giving it to me, I’ll gladly take it.*

I was just about to check my Inventory, brimming with anticipation, when—

*Knock, knock, knock.*

Along with the sound of someone knocking, a person cautiously poked his head inside.

“Captain. It’s Mujin…”

“Get lost.”

“No, that’s not what I meant.”

“Hyung’s busy. Go read some Gwiyeommi novels.”

“Oh, Captain, you read them too?”

“…”

*You little bastard.*

This wouldn’t do. Before opening the Item, I needed to open him up first.

I shot up from the bed, and Hyuk Mujin hurriedly shouted,

“Henan! It’s Henan!”

“What?”

“An investigation team came from Henan! They’re looking for you, Captain.”

“…”

*An investigation team?*

I frowned at Hyuk Mujin’s explanation, which had left out everything before and after.

*Ding.*

A familiar notification reached my ears.

[^1]: Gwiyeommi is the pen name of a romance novelist.
```
