<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0108.txt",
      "sha256": "795127a4dfbd1eda33b519378e50f46a563de8fe92cb9cdcf4943ee1d7771e54",
      "bytes": 13932
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "741ad4e1a38826afbf9fcc13a9ee9f7d15a7d5f4e98ef33f5e0d823edb3fa7a4",
      "bytes": 5151
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "99a9e89ac7c4c48f0fb9d55f8bd60a70a3365cca96d5746882c56c22f17578db",
      "bytes": 14332
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "7a826f95f3c168cd0cd05c2772541d1498b7c3d508e0b3b9fa1ba53f8734e618",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "34ab849ac7eb29392a9cf0e4da68e6f16c1567da0d1da90088189c054b916727",
      "bytes": 1221
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "f95bcc7301b343948d4c231f8e3a49e58484143247a903dda570f4a9b8db5631",
      "bytes": 2246
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a05455fcf682929936dc149653dbc807199a561412008c8adebc5f45854eca0",
      "bytes": 14426
    }
  ],
  "estimated_tokens": 17192
}
-->

# Durable State Update — Chapter 108

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 108. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 108. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 108,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 108,
    "continuity_sources": [108],
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
    "Sangdong Guild's Security Team surveils Jin Taekyung from an unidentified property; Choi Byungil's failed operation has left the team facing unresolved discipline.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is an outside B-rank Familiar mage hired by Team Leader 1.",
    "Seong Jinho is Taekyung's civilian goshiwon manager and sworn-brother-like friend; he emerged from Taekyung's capsule inside the new house, though how he entered remains unknown.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 former Hunter Training Center instructor who trained Chunsoo; he now works as a butler, though his arrival and change of occupation remain unexplained.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "Taekyung owns a two-story house in Goyang and will live there alone until Hayeon finishes her college entrance exam; Logout is active.",
    "Taekyung, Mukyung, Mujin, and Wolhwa are traveling toward the Mount Heng Sword Sect after reaching Honju.",
    "Mukyung uses a superficially learned heat-yang technique to warm Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect led by Lee Seowol, his former accuser.",
    "Hyuk Mujin is a First Rate martial artist from a tenant-farmer family, Captain of the Jin Family's Gatekeepers, deputy squad leader of White Tiger Hall's reconnaissance squad, and a candidate to become Master of the Gatekeeper Pavilion.",
    "Jin Wikyung gave Mujin fifty silver nyang for the journey; Mukyung treats hunger as training, while Taekyung's appetite causes Mujin financial anxiety.",
    "The Phoenix Inn attackers bore running-horse tattoos; Wolhwa said Lee Cheonbaek hired wandering martial artists and mounted-bandit groups during the war.",
    "Wolhwa is the Phoenix Inn's proprietress, a courtesan, Shanxi's foremost information merchant, and the Lower District Sect's Shanxi Branch Leader; she is accompanying Taekyung's group to Mount Heng.",
    "The Lower District Sect's wartime pact with the Jin Family promised Wolhwa compensation that she has not received; she seeks influence in northern Shanxi while Jin Wikyung seeks a quiet merger with Mount Heng.",
    "Wolhwa ordered the Lower District Sect to cancel its investigation into Taekyung and issue a gag order after finding no explanation for his rapid rise.",
    "Wolhwa's replacement coachman is a Level 50 First Rate martial artist who also serves as a bodyguard.",
    "Mukyung is unusually awkward and shy around Wolhwa but formally thanked her for aiding the Jin Family; she stated that proper compensation remains unpaid.",
    "The Red Wind Band is a powerful northern-plateau group led by a formidable martial artist with two hundred followers; it avoided Eight Spring Gorge and then targeted Mount Heng's weakened main base.",
    "The Mount Heng Sword Sect won the later two-day battle but lost its Young Sect Leader, and regional unrest has grown as the sect's strength declined.",
    "The travelers are sheltering in an abandoned shrine at midnight and have seen unidentified torches approaching through a thin snowstorm."
  ],
  "continuity_sources": [
    107
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong now works as a butler despite his former instructor status and exceptional ability remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "Who the torch-bearing people approaching the abandoned shrine are and what they intend remains unknown."
  ],
  "safe_through": 107,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; render 김화종's 춘수 and 교관님 as Chunsoo and Instructor.",
    "Render 1번 훈련생 as Trainee Number One and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 and 계용옥미갱/계용옥미앵 as Phoenix Inn and chicken-and-corn soup.",
    "Render 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; render 적풍단 as Red Wind Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's playful Young Master forms for Taekyung and use Young Hero Jin for her 진 소협 address to Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures."
  ],
  "version": 1
}
```

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
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |

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
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 월화     | **Wolhwa**         |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 마적     | **mounted bandits**                              |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 은인     | **Benefactor**                               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 107
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 107
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 107
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃108화



‘사냥꾼?’

월화의 짐작은 절반만 맞았다. 사냥꾼은 사냥꾼인데, 불청객들의 정체는 조금 더 특별하고 훨씬 더 악랄했다.

“빨리빨리 걸어라, 이놈들아.”

“사내라는 것들이 이렇게 비리비리해서 어디다 써?”

머릿수는 총 열 명. 하나같이 험상궂은 얼굴에, 병장기로 무장까지 했다. 그들의 선두에선 굴비처럼 밧줄로 묶인 포로들이 비틀거리고 있었다.

퍽, 퍽퍽!

“아이고, 대혀업!”

“갑니다, 가고 있으니까 제발 그만 좀…….”

“허, 그만? 이놈들이 아직도 정신이 덜 들었구나.”

“어허, 적당히 때려. 어디 한 군데 부러지기라도 하면 값 떨어진다. 가뜩이나 조그마한 놈들이라 제값도 못 받게 생겼구먼.”

“곡마단(曲馬團)에 팔아먹으면 그럭저럭 받겠지. 후딱 들어가서 화주나 한잔하자고.”

“아따, 생각만 해도 침이…… 근데 저건 뭐여?”

인간 사냥꾼들의 발걸음이 우뚝 멈췄다. 사당 앞에 세워져 있는 사두마차를 응시하던 눈동자들이 스르륵 옆으로 옮겨 간다.

그들의 시선 끝에 나와 월화가 있었다.

“……누구쇼?”

우두머리로 보이는 놈의 질문에 내가 나섰다.

“지나가던 과객.”

“과객이라. 요즘 같은 시기에 돌아다니면 위험한데.”

번들거리는 눈빛이 스스로가 위험한 놈이란 걸 말해 준다.

물론 그래 봤자 겨우 25레벨이라 내게는 위험 축에도 못 끼지만.

“이야, 사두마차에 기막힌 미녀까지. 있는 집 공자님이신가 봐?”

가까이 다가가서 확인했다면 마차에 새겨진 태원진가의 문장을 확인할 수 있었겠지만, 지금은 시커먼 밤이었고 놈은 뛰어난 안력(眼力)의 소유자가 아니었다.

“없는 집 자식은 아니지.”

“거참. 아까부터 말씀이 짧으시네.”

우두머리가 갈라진 입술을 핥았다. 슬슬 열이 오르는 모양이지만 아직은 나에 대한 경계를 풀지 않고 있다.

“뭐, 됐고. 이곳은 우리가 며칠 전부터 머무르던 곳인데…… 어쩌겠소?”

“뭘?”

“뭐긴, 약간의 성의를 보여 주면 자리를 내어 드릴 수 있다는 거지.”

“누가 들으면 이 사당이 그쪽 건 줄 알겠네.”

“버려진 곳이니 먼저 차지하는 사람이 임자 아닌가?”

“그럼 부동산 내용 증명서 떼 와.”

“뭐?”

우두머리가 어리둥절한 얼굴로 수하들을 돌아봤다. 생전 처음 듣는 용어일 테니 당연한 일이다. 하지만 아는 놈이 있을 리가 있나.

부동산 내용 증명서에 관해 수군거리는 놈들을 향해 쯧쯧 혀를 찼다.

“증명 못 하겠으면 곱게 돌아가라. 거기 잡아 둔 사람들은 풀어 주고.”

“……선을 넘는군. 호위무사라도 기다리나?”

“그런 거 없어.”

“그럼 뭘 믿고?”

“나.”

우두머리의 시선이 내 텅 빈 두 손을 향한다.

“병장기도 없이?”

“너희 정도야 주먹으로 충분하니까.”

“도련님이 어디서 한 수 배우긴 했나 본데…… 무림을 너무 우습게 보는 거 아닌가?”

“무림은 안 우습지. 그냥 너희가 우스운 거야.”

말과 함께 환하게 밝혀진 횃불을 향해 발을 내디딘 그 순간, 얌전히 잡혀 있던 포로들이 괴성을 내질렀다.

“어, 어어어?”

“으어어어! 대형! 대형!”

“이 자식들이 미쳤나. 다들 입 안 닥쳐!”

포로들의 격한 반응에 뒤에 선 놈들이 단검을 뽑아 목에 가져다 댔다. 우두머리가 경계심 어린 눈빛으로 나를 응시했다.

“아는 놈들인가?”

“아니, 태어나서 처음 보는데.”

반응이 너무 갑작스러워서 나까지 당황할 정도다. 그리고 갑자기 대형이라니?

“대혀어엉! 접니다! 저흽니다!”

“이놈들은 그쪽을 아는 것 같은데?”

“그거야 그냥 구해 달라고…… 어라?”

나는 포로들을 유심히 바라봤다. 어린애처럼 작은 키에 하나같이 못생긴 얼굴. 어디서 본 것 같기도 하다.

‘체형이 고블린을 닮아서 낯이 익은 건가?’

잠깐만. 고블린?

문득 오래전의 기억이 떠오른다. 아니, 사실 그리 오래된 기억도 아니다. 불과 몇 달 전 튜토리얼 퀘스트에서 있었던 일이니까.

“설마 그, 천력부랑 같이 있었던?”

포로들, 아니 천력부 장삼의 부하였던 오색귀(五色鬼)가 미친 듯이 고개를 끄덕였다.

“맞습니다, 저흽니다!”

“대형! 살려 주십시오!”

이놈들을 여기서 보게 될 줄이야. 황당해하는 내게 뒤에서 상황을 지켜보던 월화가 물었다.

“진 공자가 아는 사람들이에요?”

“일단은 구면이네요.”

인신매매범과 산적이라. 우열을 가릴 수 없는 조합이다.

방금까지는 구해 줄 생각이었는데 지금은 살짝 고민되네.

“대혀어어엉!”

“저흴 버리실 생각이십니까!”

“그날 이후 산적질도 그만두고 착하게 살았습니다!”

“…….”

눈치 하나는 귀신이다. 하긴, 천력부가 죽었을 때도 바로 항복해 버린 놈들이니 오죽할까.

“구해 줄 건가요?”

“쓰읍. 일단 구하긴 해야 할 것 같아요.”

그날 이후 새사람이 됐다는데 이대로 보내기에는 영 찝찝하다. 무엇보다 현직 인신매매범보다는 전직 산적이 훨씬 낫지.

그러자 우리의 대화를 들은 우두머리가 으르렁거리는 목소리로 끼어들었다.

“구해? 네놈이?”

“다 들어 놓고 뭘 또 물어봐. 너 인생 피곤하게 사는구나?”

“이 애새끼가 보자 보자 하니까…….”

차차창!

우두머리가 창을 겨누자 수하들도 무기를 빼 들었다. 월화가 짐짓 겁먹은 얼굴로 내 옆구리에 달라붙는다.

“어머, 무서워. 나 꼭 지켜 줘야 해요?”

보호 본능을 불러일으키는 촉촉한 눈망울. 간절한 표정.

월화의 실체를 아는 나로서는 기가 차는 광경이지만 놈들은 침을 꿀꺽 삼켰다.

“널 죽여야 하는 이유가 하나 더 늘었군.”

우두머리의 끈적끈적한 눈빛에 월화가 꺅, 비명을 질렀다.

“어떡해, 어떡해! 소녀, 너무 무서워요!”

“허허, 너무 겁먹지 말거라. 내 비록 일평생 거칠게 살았어도 마음만은 비단결처럼 고운 사내라는 걸 알게 될 테니. 잠시 후에 몸으로 대화를 나눠 보자꾸나.”

“어, 그전에 나 좀 보자.”

더러운 주둥이를 찢어 놔야 다시는 저딴 소리를 못 하지.

놈을 향해 성큼성큼 걸어가다가 문득 발걸음을 멈췄다. 그런 내 모습을 본 우두머리가 껄껄 웃었다.

“왜, 막상 싸우려니까 겁이 나나? 하지만 이미 늦었어.”

“그러게. 너, 진짜 큰일 났다.”

“……뭐?”

나는 어리둥절해하는 놈을 향해 활짝 웃어 주었다.

“좆 됐다고. 인마.”

말이 끝난 그 순간, 땅이 울림과 동시에 강력한 바람이 휘몰아쳤다.

쿵, 쐐애애액!

말 그대로 찰나에 불과한 시간.

무서운 속도로 나와 월화를 스쳐 간 그것은 어느새 우두머리의 앞에 서 있었다.

“다시 한번 말해 봐라.”

진무경. 그의 전신에서 뿜어져 나온 어마어마한 기파(氣波)가 장내를 짓눌렀다. 우두머리가 파랗게 질린 얼굴로 손을 덜덜 떨었다.

“요, 용서. 제발…….”

차가운 목소리가 대답했다.

“한참 늦었어.”



* * *



어쩌면 진무경은 우리 중 최고의 비폭력주의자일지도 모른다. 불과 십여 초 만에 이어질 모든 불필요한 싸움을 종결지었으니까.

“하, 항복, 항복하겠습니다.”

“제발 살려 주십시오. 제발 목숨만은…….”

공포에 질린 얼굴. 모두 다리가 풀려 자리에 주저앉았고, 누군가가 지린 소변은 언덕 아래로 흘렀다.

그건 오색귀도 마찬가지였다.

“시끄럽다.”

진무경이 얼굴에 묻은 피를 닦아 내며 툭 던진 한마디에 죽음 같은 침묵이 내리깔린다. 눈 한쪽이 시퍼렇게 멍든 혁무진이 내게 속삭였다.

“저 지금 살아 있는 거 맞습니까?”

“어, 귓가에 숨결 닿는 거 소름 돋으니까 좀 떨어져.”

“아까 전만 해도 이렇게 개처럼 맞을 수가 있나, 하는 생각이었는데 지금은…….”

꿀꺽, 마른침을 삼키는 혁무진의 시선은 쓰러진 우두머리를 향해 고정되어 있었다.

“흐윽, 흐으윽.”

사지가 부러지고 단전(丹田)이 파괴당한 그는 힘겹게 숨을 몰아쉬는 중이었다. 잘만 요양하면 다시 걸어 다닐 수는 있겠지만 무인으로서의 생명은 끝장이다.

기감으로 파악한 레벨창이 그 증거였다.



[Lv.2 이삼]



감시자들이 패밀리어로 쓰던 똥파리가 1레벨이었지, 아마.

한때 일류에 근접했던 25레벨의 무인을 산송장으로 만들어 버린 범인은 아까부터 계속 이쪽을 힐끗거리고 있다.

“조장님, 저 좀 살려 주세요. 이공자님께서 피가 부족하신가 봐요.”

“헛소리하지 말고 쟤나 좀 적당한 곳에 옮겨 놔. 저러다가 죽겠다.”

“죽어도 싼 놈 아닙니까? 멀쩡한 양민들 팔아먹던 놈들이잖아요.”

“그래도 옮겨. 아직 살아 있잖아.”

내가 무림과 현대를 오가며 느낀 가장 큰 괴리감 중 하나가 바로 살인(殺人)에 관한 문제였다.

27년간, 법과 질서가 존재하는 사회에서 살았던 나다.

날붙이로 적을 죽이는 법을 단련해 왔지만 그 대상은 몬스터였지, 살아 있는 인간이 아니었다.

‘분명히 그랬는데…….’

이제는 몇 명을 죽였는지 기억도 안 난다. 지금까지 내 손에 죽어 나간 적들이 NPC가 아닌 진짜 사람일지도 모른다는 걸 깨달았을 때도 큰 죄책감은 들지 않았다.

‘적이었으니까. 저들도 날 죽이려고 했으니까.’

헌터로 살아왔기 때문인지, 무림의 방식에 익숙해진 건지는 잘 모르겠다. 다만 무덤덤한 마음과 단순한 자기 합리화에 스스로 놀랐을 뿐.

‘지금은 이 정도로도 괜찮겠지.’

나는 전혀 다른 두 세계를 살아가는 중이다. 어설픈 불자(佛子) 흉내를 낼 정도로 여유로운 상황이 아니다.

들러붙는 생각을 떨쳐 내며 주저앉아 있는 놈들을 향해 다가갔다.

“히익!”

“흐아악, 살려 주십쇼, 대형!”

“이 자식들은 구해 주려고 해도 난리네. 가만히 있어 봐.”

밧줄을 풀어 주자 자유의 몸이 된 오색귀가 후들거리는 다리로 일어났다.

“가, 감사합니다.”

“평생 은인으로 모시겠습니다!”

“은인으로 모시긴 개뿔이. 그나저나 어쩌다가 이런 놈들한테 잡힌 거냐? 그것도 다섯 명이 한꺼번에.”

오색귀 놈들이 체구가 작긴 해도 명색이 성인 남자다. 천력부를 따라 산적질 할 정도의 수준은 된다.

“아니, 저 그게.”

“……?”

뭐지, 이놈들.

머뭇거리는 태도에 이상함을 감지한 나는 가장 가까이 있는 인신매매범의 멱살을 붙잡고 끌어올렸다.

“이놈들 어떻게 붙잡았어?”

“저, 저잣거리에서 저희 전낭을 슬쩍 하려던 걸 붙잡았습니다.”

“…….”

이런 십색귀들을 봤나. 산적 관두고 농사라도 짓나 했더니 직종을 바꾼 거였어?

“변명해 봐.”

날카로운 내 시선에 다섯 놈이 눈알을 뒤룩뒤룩 굴렸다.

“그, 그러니까.”

“대형, 저희 같은 놈들은 배운 게 그런 것뿐이라.”

“그, 그래도 시작한 지 얼마 안 됐습니다!”

“착실하게 일하려고 했는데 영 신통치가 않아서…… 딱 한탕만 치고 빠지자 했던 게 그만.”

“마적단 놈들인 줄 알았으면 건드리지도 않았죠. 저희도 피해잡니다. 대형, 제발 한 번만 용서해 주십쇼!”

이놈들을 어떻게 처리해야 하나 고민하던 나는 익숙한 단어에 잠시 멈칫했다.

“뭐라고?”

“진짜 딱 한 번만 더 용서해 주시면 착실하게 살겠습니다!”

“아니, 그거 말고. 저놈들이 뭐라고?”

“아, 마적단 말씀이십니까요?”

“그래, 그거.”

“저희도 잡힌 후에야 들었습니다. 웬 왈패 무리가 기루에서 은자를 뿌리며 다니기에 따라붙었는데…… 마적들 사이에서도 흉악하기로 소문난 적풍단(赤風團) 놈들이었지 뭡니까.”

“적풍단? 확실해?”

“예. 제 귀로 똑똑히 들었습니다. 맞지?”

다른 놈들도 앞다퉈 한 마디씩 보태기 시작했다.

“내일 날이 밝자마자 떠날 거라고도 했습니다.”

“산음(山陰)까지 가려면 쉬지 않고 달려야 한다고. 괜히 늦었다가 목 달아나는 거 아니냐고 걱정까지 하던데요.”

“그렇단 말이지.”

어제, 그리고 오늘. 이틀 연속으로 만난 마적이 하필이면 적풍단 소속인 것도 공교로운데, 산음은 항산검문의 본거지가 있는 응현(應現)과 가까운 곳이다.

“이 녀석들 말이 모두 사실이냐?”

내 오른손에 멱살이 붙잡혀 있던 인신매매범, 아니 적풍단의 마적이 덜덜 떨며 고개를 끄덕인 그 순간이었다.

삐이익!

날카로운 울음소리와 함께 한 마리의 매가 사당 앞에 내려앉았다. 발목에 묶인 자그마한 원통이 눈에 들어온다.

‘전서응.’

이거 어째 분위기가 묘하게 돌아가는데.
```

## Final English reading copy

```markdown
# Chapter 108

*Hunters?*

Wolhwa’s guess was only half right. They were hunters, all right—but the uninvited guests were something more special and far more vicious.

“Move it, you bastards.”

“Who can do anything with men as scrawny as you?”

There were ten of them in all. Every one had a rough-looking face and was armed with a weapon. At the front of their group, prisoners tied together with rope like a string of dried fish staggered along.

*Thud! Thud-thud!*

“Ugh, Boss!”

“We’re coming, we’re coming, so please stop already…”

“Huh, stop? These bastards still haven’t come to their senses.”

“Hey, take it easy. If you break something, their price drops. They’re small to begin with, so it looks like we won’t get full value for them.”

“We should get a decent price if we sell them to a circus troupe. Let’s hurry inside and have a drink.”

“Ah, my mouth waters just thinking about it… But what’s that?”

The human hunters came to an abrupt stop. Their eyes, which had been fixed on the four-horse carriage parked in front of the shrine, slowly shifted to the side.

At the end of their gazes stood Wolhwa and me.

“…Who are you?”

I stepped forward at the question from the man who appeared to be their leader.

“Just a traveler passing through.”

“A traveler. It’s dangerous to be wandering around at a time like this.”

The gleam in his eyes told me he was a dangerous man.

Of course, at Level 25, he didn’t even qualify as a threat to me.

“Wow, a four-horse carriage and a gorgeous woman. You must be a Young Master from a wealthy family, huh?”

If he had come closer to inspect it, he could have seen the crest of the Jin Family of Taiyuan carved into the carriage. But it was pitch-black outside, and he didn’t possess particularly sharp eyesight.

“I’m not from a poor family.”

“Well now. You’ve been awfully informal with me from the start.”

The leader licked his split lips. He seemed to be getting irritated, but he still hadn’t let down his guard around me.

“Whatever. This is a place we’ve been staying in for several days… What are you going to do?”

“Do about what?”

“What do you think? If you show us a little sincerity, we might let you have the place.”

“Anyone listening would think you owned this shrine.”

“It’s abandoned. Doesn’t that mean whoever claims it first owns it?”

“Then go get a certified property document.”

“What?”

The leader turned toward his men with a bewildered expression. Naturally. They had probably never heard the term in their lives. But it wasn’t as though any of them would know what it meant.

I clicked my tongue at the men whispering among themselves about the certified property document.

“If you can’t prove it, then leave quietly. And release the people you’ve tied up.”

“…You’re crossing the line. Are you waiting for bodyguards?”

“I don’t have any.”

“Then what are you relying on?”

“Me.”

The leader’s gaze shifted to my two empty hands.

“Without even a weapon?”

“People at your level? My fists are enough.”

“Looks like the Young Master learned a move or two somewhere… But aren’t you taking Murim a little too lightly?”

“Murim isn’t something to laugh at. You are.”

The moment I stepped toward the brightly burning torch, the prisoners who had been quietly restrained began screaming.

“Wh-what?”

“Boss! Boss!”

“You bastards gone crazy? Shut your mouths!”

The men in the rear drew daggers and held them to the prisoners’ throats in response to their violent reaction. The leader stared at me with wary eyes.

“Do you know them?”

“No. I’m seeing them for the first time in my life.”

Their sudden reaction had even caught me off guard. And why were they suddenly calling me Boss?

“Bosss! It’s me! It’s us!”

“These men seem to know you.”

“They’re just asking me to save them… Huh?”

I looked closely at the prisoners. They were all short as children and had uniformly ugly faces. They looked vaguely familiar.

*Is it because their body shapes resemble goblins?*

Wait. Goblins?

A memory from long ago suddenly came to mind. No, it wasn’t actually that long ago. It had happened only a few months earlier, during the tutorial Quest.

“Don’t tell me… You were with the Heavenly Axe?”

The prisoners—or rather, the Five-Colored Ghosts[^1] who had once been Jang Sam the Heavenly Axe’s subordinates—nodded frantically.

“That’s us!”

“Boss! Please save us!”

I never expected to run into these bastards here. As I stood there dumbfounded, Wolhwa, who had been watching the situation from behind, asked,

“Are these people acquaintances of Young Master Jin?”

“We’ve met before, at least.”

Human traffickers and bandits. It was hard to say which was worse.

Until a moment ago, I had been thinking of saving them. Now I was having second thoughts.

“Bosssss!”

“Are you planning to abandon us?”

“We quit being bandits after that day and have lived good lives ever since!”

“…”

Their ability to read the situation was almost supernatural. No wonder. They had surrendered immediately when the Heavenly Axe died, after all.

“Are you going to save them?”

“Tsk. I think we have to, at least.”

They said they had become new men after that day, and it felt wrong to leave them like this. More importantly, former bandits were far better than active human traffickers.

The leader, who had overheard our conversation, interrupted with a growl.

“Save them? You?”

“You heard the whole thing. Why ask again? You must live a tiring life.”

“You little shit, I’ve been letting you run your mouth, but…”

*Clang!*

The leader leveled his spear at me, and his men drew their weapons as well. Wolhwa clung to my side with a deliberately frightened expression.

“Oh my, I’m scared. You have to protect me, don’t you?”

Her moist eyes stirred a man’s protective instinct. Her expression was pleading.

To someone who knew Wolhwa’s true nature, it was an absurd sight. But the men swallowed hard.

“There’s one more reason I have to kill you.”

At the leader’s lecherous gaze, Wolhwa let out a shriek.

“Oh no, oh no! This maiden is so scared!”

“Ho ho, don’t be so frightened. Though I may have lived a rough life, you’ll soon learn that I’m a man with a heart as soft as silk. In a little while, we can have a conversation with our bodies.”

“Before that, deal with me.”

I needed to rip that filthy mouth open so he would never say anything like that again.

I strode toward him, then suddenly stopped. Seeing that, the leader burst out laughing.

“What’s wrong? Are you scared now that we’re actually going to fight? But it’s already too late.”

“Yeah. You’re really screwed.”

“…What?”

I gave the bewildered man a broad smile.

“I said you’re fucked, asshole.”

The moment I finished speaking, the ground shook, and a powerful wind whipped through the area.

*Boom—whoosh!*

It lasted no more than an instant.

The figure that swept past Wolhwa and me at terrifying speed was already standing in front of the leader.

“Say that again.”

Jin Mukyung.

An overwhelming wave of qi poured from his entire body and crushed the entire scene. The leader’s face turned deathly pale, and his hands began to tremble.

“F-forgive me. Please…”

The cold voice answered.

“You’re far too late.”

* * *

Perhaps Jin Mukyung was the greatest pacifist among us. In just over ten seconds, he had put an end to all the unnecessary fighting that would have followed.

“S-surrender! We surrender!”

“Please spare us! Please, just spare our lives…”

Their faces were frozen with terror. Everyone’s legs gave out, and they collapsed where they stood. Someone’s urine trickled down the hill.

The Five-Colored Ghosts were no different.

“Quiet.”

Jin Mukyung wiped the blood from his face and tossed out a single word. A deathly silence descended.

Hyuk Mujin, one eye bruised deep blue, whispered to me,

“Am I actually alive right now?”

“Yeah. Your breath against my ear is giving me goose bumps, so move away.”

“Just a moment ago, I was thinking, *How can someone get beaten like a dog this badly?* But now…”

*Gulp.*

Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader.

“Hng… Hng…”

With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over.

The Level window I sensed through Qi Sense was proof.

> **System**
>
> **Level 2 — Lee Sam**

*The dung flies the watchers used as Familiars were Level 1, if I remember correctly.*

The culprit who had turned a Level 25 martial artist who had once been close to First Rate into a living corpse had been sneaking glances in our direction for a while.

“Captain, please save me. I think the Second Young Master is still short on blood.”

“Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.”

“Isn’t he a bastard who deserves to die? They were selling perfectly innocent commoners.”

“Even so, move him. He’s still alive.”

One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people.

For twenty-seven years, I had lived in a society where law and order existed.

I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans.

*I was sure that was the case…*

Now I couldn’t even remember how many people I had killed. Even when I realized that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt particularly guilty.

*They were enemies. They were trying to kill me too.*

I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification.

*For now, maybe this much is okay.*

I was living in two entirely different worlds. This wasn’t a situation where I had the leisure to put on an awkward act as a Buddhist.

Shaking off the thoughts clinging to me, I approached the men cowering on the ground.

“Eek!”

“Uaaagh! Save me, Boss!”

“These guys cause a commotion even when I’m trying to save them. Hold still.”

I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs.

“Th-thank you.”

“We’ll regard you as our Benefactor for the rest of our lives!”

“Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?”

The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe.

“Um, well…”

“…?”

What was wrong with these guys?

Sensing something strange in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up.

“How did you catch these men?”

“We caught them trying to steal our money pouches in the marketplace.”

“…”

What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations?

“Explain yourselves.”

Under my sharp gaze, the five men rolled their eyes back and forth.

“W-well…”

“Boss, people like us only know how to do this.”

“Even so, we only started recently!”

“We tried to work honestly, but things didn’t go very well… We said we’d pull just one job and get out, but then…”

“If we’d known they were mounted bandits, we wouldn’t have touched them. We’re victims too. Boss, please forgive us just this once!”

As I wondered what to do with these men, a familiar word made me pause.

“What did you say?”

“We’ll live honestly if you forgive us just one more time!”

“No, not that. What did they say?”

“Ah, do you mean the mounted-bandit group?”

“Yes. That.”

“We only heard after we were captured. Some bunch of ruffians were throwing silver around at a pleasure house, so we followed them… But they turned out to be members of the Red Wind Band, infamous for their viciousness even among mounted bandits.”

“The Red Wind Band? Are you sure?”

“Yes. I heard it clearly with my own ears. Didn’t I?”

The others began eagerly adding their own pieces.

“They said they were leaving as soon as dawn broke tomorrow.”

“They said they’d have to travel nonstop to reach Saneum. They were even worried that they might lose their heads if they arrived late.”

“So that’s how it is.”

Yesterday and today.

It was already an uncanny coincidence that the mounted bandits I had encountered two days in a row happened to belong to the Red Wind Band. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters was located.

“Are these men telling the truth?”

The human trafficker held by the collar in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded with a trembling head.

That was when it happened.

*Shriek!*

A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye.

*A messenger hawk.*

This was getting strange.

[^1]: A nickname meaning “Five-Colored Ghosts.”
```
