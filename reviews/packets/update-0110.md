<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0110.txt",
      "sha256": "7742a210cb4f15ceac14b18de6bae64f7845724c1646668f77a31fbf76c60ccc",
      "bytes": 12734
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "81ade0489eba062402eaf3f670bda121b7abedea9a3a9ff09eca652ffbbcf4d4",
      "bytes": 3465
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3b8ae8f789f325565647fb5a5f7e97d73a47ded8ca1e9160ba54807dd1af477b",
      "bytes": 15322
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e72bc10fe5f550bd70d357aa29afefeadb92370c78cdf7318495251ab705c616",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "715a383b4ad81f86f82155a8df8037262bdb2e9034a3faaf0a6f1e4c772daa36",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c41bd91d265ef3b27ab2aeb55ba202ff129edfb9feba01db09b4b71b6160fccd",
      "bytes": 24117
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "4c0a797452545b76d61c8629b4330eab80fd2cf5fe62bd9d0d56204c6727c193",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "95f6353519d32409a7215cf4407db935be764742d13c9e91b1e7979c27c46b48",
      "bytes": 3101
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "91896def3a6b6f762138302223842c5b9d33f8a6639ec8965ab13b45b6e7abbf",
      "bytes": 473
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "6bcdccaa18cf3ad3da922dd237ec6b5593c78e661f5ad7b3c5156191b4de2c32",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "07d223b8bbd7e60358ac166fc2d1636bdfeb290653c63428fef86d33c99808a7",
      "bytes": 14933
    }
  ],
  "estimated_tokens": 17688
}
-->

# Durable State Update — Chapter 110

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 110. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 110. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 110,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 110,
    "continuity_sources": [110],
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
    "Taekyung, Mukyung, Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect.",
    "The Five-Colored Ghosts and surviving mounted bandits are being taken to a nearby Lower District Sect branch.",
    "A messenger hawk from the Lower District Sect's Sakju Branch delivered intelligence to Wolhwa.",
    "The Red Wind Band is moving south with approximately two hundred members.",
    "The Red Wind Band has crossed Datong and destroyed the Mount Heng Sword Sect's Datong Branch with no survivors.",
    "Pung Yang is the Red Wind Band Leader and commands his force with ruthless authority.",
    "Chunsam is a First Rate Lower District Sect martial artist who served as the group's carriage driver.",
    "Wolhwa uses lethal interrogation to obtain information from hostile mounted bandits.",
    "The Mount Heng Sword Sect has lost nearly eighty percent of its strength in the war with the Jin Family of Taiyuan.",
    "The Red Wind Band's attack on Mount Heng is expected within one or two days.",
    "The Mount Heng Sword Sect's main hall doors have exploded as the attack begins.",
    "The Quest difficulty has changed to Peak."
  ],
  "continuity_sources": [
    109
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong now works as a butler despite his former instructor status and exceptional ability remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "What will happen inside the Mount Heng Sword Sect's main hall after its doors are destroyed remains unknown."
  ],
  "safe_through": 109,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; 김화종's 춘수 and 교관님 as Chunsoo and Instructor; 1번 훈련생 as Trainee Number One; and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year; 봉황객잔 as Phoenix Inn; 계용옥미갱 and 계용옥미앵 as chicken-and-corn soup; and 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; 적풍단 as Red Wind Band; 적풍단주 as Red Wind Band Leader; and 토호단 as Earth Tiger Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's Young Master forms for Taekyung and Young Hero Jin for Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures.",
    "Render 오색귀 as Five-Colored Ghosts, 이삼 as Lee Sam, 전서응 as messenger hawk, and 대형 as Boss.",
    "Render 추종향 as tracking scent, 대동 as Datong, 풍양 as Pung Yang, 춘삼 as Chunsam, 철검대주 as Iron Sword Squad Leader, 대항산검문 as great Mount Heng Sword Sect, and 대동지부 as Datong Branch.",
    "Render 절정 as Peak, 일류 as First Rate, 일격 as One Strike, and 단주 as Leader."
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
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |

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
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 대주     | **Squad Leader** / **Commander**             |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 109
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 109
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 106
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 107
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 109
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; leader of the Mount Heng Sword Sect

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 103
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant
- **Personality:** Not established in Chapter 74
- **Voice:** Not established in Chapter 74
- **Relationships:** Lee Cheonbaek's daughter; younger sister of the deceased Young Sect Leader and Lee Seogeun

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 109
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃110화



쾅!

굉음과 함께 나타난 것은 장대한 체구의 중년인이었다.

억세게 뻗친 눈썹 아래, 성난 맹수처럼 호목(虎目)을 부릅뜬 그가 좌중을 쓸어 본다.

“방금 헛소리를 지껄인 자가 누구냐?”

이 자리에 모인 이들은 모두 항산검문의 중진.

전임자만큼은 아니어도 일류의 무공과 일정 이상의 경륜을 지닌 이들이다. 그러나 그들조차도 목을 움츠리고 시선을 피하기 바빴다.

눈앞의 중년인은 그럴 자격이 충분히 있는 사람이니까.

‘제길, 하필이면 항산호(恒山虎)한테…….’

호사가들이 이르길, 항산에는 두 마리 맹수가 산다고 했다.

혈랑검과 항산호. 절친한 벗이자 서로가 넘어야 할 벽.

중년인, 철무백은 이미 수십 년 전부터 항산의 호랑이라 불리는 절정 고수였다.

“어느 놈이냐 물었다!”

그 포효 같은 외침에 항산검문의 중진들은 전신의 털이 쭈뼛 곤두섰다.

철무백이 한번 꼭지가 돌면 친우였던 이천백조차 자리를 피한다고 했다. 하물며 무공과 연배에서 한참 뒤처지는 그들이니 두말할 것도 없다.

“일치단결하여 저 말 도적놈들을 몰아내도 모자랄 판에, 감히 천백의 유지를 어기고 역심을 품어?”

화염이 쏟아질 듯한 눈빛에 항산검문의 중진들은 불에 덴 것처럼 화들짝 놀랐다.

“처, 철 대협. 오해십니다.”

“저희가 어찌 감히 역심을 품겠습니까.”

“그럼 내 나이가 늙어 귀가 어두워진 것이냐?”

그 순간, 대전 안의 사람들은 갈증을 느꼈다. 단순한 착각이 아니라 철무백이 뿜어내는 가공할 만한 열양지기(熱陽地氣) 때문이었다.

‘이런 미친.’

‘도대체 뭘 얼마나 처먹었기에 이런 무지막지한 공력이…….’

단순히 가까이 있는 것만으로도 숨이 막히고 땀이 줄줄 흐른다. 항산호. 약관 무렵부터 광활한 산맥의 어딘가에서 홀로 무공을 익혔다는 절정 고수의 진면목이 드러나는 순간이다.

“훅, 후우욱.”

“대협, 부디 고정하십, 후욱.”

거친 숨을 몰아쉬는 항산검문의 중진들, 그리고 용서의 기미 없이 그들을 노려보는 절정 고수.

대전 안의 공기가 용암처럼 들끓어 오르려던 그때였다.

“철 숙부, 더워요.”

시냇물처럼 청량한 목소리와 철무백의 소매를 잡아당기는 희고 가느다란 손가락. 그와 동시에 분노로 주름져 있던 철무백의 미간이 누군가 잡아당긴 것처럼 쫙 펴졌다.

“마, 많이 더웠느냐?”

“네, 숨도 못 쉬겠어요.”

“이런, 내가 미처 네 생각을 못 했구나. 지금은 어떠하냐?”

“한결 나아졌어요. 고마워요, 철 숙부.”

“그런 말은 하지 말거라. 소월이 너를 지키는 게 내 할 일인 것을.”

철무백의 강대한 열양지기가 사그라든다.

그제야 곳곳에서 참았던 숨이 터져 나왔다. 땀으로 흠뻑 젖은 사람들은 정신을 차리고 난 뒤에 철무백이 혼자가 아님을 깨달았다.

“아, 아가씨.”

“아가씨를 뵙습니다.”

황급히 자리에서 일어나 예의를 표하는 중진들의 모습에 눈썹을 치켜뜨는 철무백. 그러나 ‘아가씨’가 한발 빨랐다.

“철검대주님, 수문각주님. 두 분께 마지막으로 말씀드릴게요.”

철무백의 거구에 가려져 보이지 않던 그녀가 모습을 드러낸다. 마르고 늘씬한 체구. 푸른색 궁장 밑단이 바닥을 스칠 때마다 사각거렸다.

“호칭을 바꾸세요. 아가씨가 아니라 문주님, 으로.”

서리가 내려앉은 듯한 그녀의 눈빛을 마주한 사람들은 잠시 잊고 있던 사실 하나를 떠올렸다.

‘아, 그랬지.’

혈랑검 이천백.

이소월은 그의 피를 가장 진하게 이어받은 자식이다.



* * *



나는 승마에 관해서는 문외한이다. 무림에 온 후에야 몇 번 타 본 정도지. 현대에서 승마는 부자들에게만 허락된 귀족 스포츠나 다름없어서 접해 볼 기회가 없었다.

하지만 신체 능력이 워낙 좋은 데다가 잘 훈련된 말을 타고 있어서 그런지, 격렬한 질주 중에도 시스템창을 볼 만큼 여유가 있었다.

‘퀘스트창 오픈.’

띠링.



퀘스트



[어제의 적, 오늘의 동지]

모든 진실이 밝혀진 지금, 항산검문은 적이 아니라 손을 잡아야 할 동지입니다. 곧 다가오는 원단에 그들을 태원진가로 초대하십시오.



등급 : 절정

제한 : 진태경

임무 : 초대장 전달 (미완료)

보상 : ???

실패 : 없음





퀘스트는 유동적이다. 상황에 따라서 돌발 퀘스트가 발생하기도 하고 지금처럼 퀘스트가 갱신되기도 한다.

‘등급 상향 조정이라.’

퀘스트 등급이 일류에서 절정으로 바뀌었다는 것은 항산검문으로 가는 길이 녹록지 않아졌다는 걸 의미했다.

예를 들자면 적풍단이라든지. 혹은 적풍단이라든지. 아마 적풍단…… 됐다. 더 말해 봤자 마음만 아프다.

‘이 동네는 하루하루가 살얼음판이 따로 없네.’

간만에 쉬운 퀘스트 하나 받나 했더니 또 일이 터졌다.

하지만 예전만큼 초조하지 않은 이유는, 진무경이라는 든든한 존재 덕분도 있지만 나 자신이 강해졌기 때문이다.

‘상태창 오픈.’

띠링.



상태창



[Lv.55 진태경]

직업 : 일류 무인

명성 : 1300 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 196 (+25)체력 : 195 (+25)

민첩 : 192 (+25)지력 : 35(+25)

매력 : 35(+25)공력 : 15년

맷집 : 155(+25)

잔여 포인트 : 0





‘크으, 주모.’

혼자 잘 컸다, 잘 컸어.

각각 200포인트에 육박하는 근력, 민첩, 체력은 보기만 해도 배가 부르고, 진무경에게 두들겨 맞으면서 생겨난 맷집도 잘 크고 있다.

‘칭호 옵션 효과도 빵빵하고. 이 정도면 충분해.’

지금까지는 살기 위해 스탯을 올렸다. 퀘스트 하나 진행할 때마다 온갖 위기가 삼각파도처럼 밀려오는데 매력과 지력에 포인트를 투자할 여력이 있었을 리가.

‘지력 올려서 아이큐 180 되면 창을 과학적으로 찌르는 것도 아니고.’

매력도 마찬가지다. 조필이나 대장로가 얼굴 좀 잘생겼다고 살려 줄 것 같진 않거든.

물론 올려 둔다면 나중에 어떤 식으로든 도움이 되겠지만, 당장 목숨이 간당거리는 와중에 비전투 스탯에 투자할 용기가 없었다.

‘이제 내 한목숨 지키는 건 어느 정도 가능하다.’

이번 퀘스트만 끝나면 공력과 비전투 스탯에 신경을 써 볼 생각이다.

안 그래도 조필을 쓰러트리고 얻은 [열화신단]을 포함한 아이템들이 인벤토리에 고이 잠자고 있다.

‘물론 잘못 먹으면 골로 가겠지만.’

그때 선두에서 달려가던 월화가 개울을 발견하고 멈춰 섰다.

“잠시만 쉬어 갈게요. 말들이 너무 지쳐서.”

시간이 얼마나 흘렀을까?

사당에서부터 쉬지 않고 달리다 보니 동이 트고 해가 중천에 걸렸다. 중간에 근력과 체력이 올랐다는 시스템 메시지도 두 번이나 뜰 정도였으니 강행군은 강행군이었던 모양이다.

“후. 엉덩이 아파 죽겠네요. 이럴 줄 알았으면 농부가 아니라 마부 아들로 태어났어야 했는데.”

말이 휴식하는 틈을 타 혁무진이 털썩 주저앉았다. 일행 중 가장 레벨이 떨어지는 녀석이니만큼 체력 소모가 눈에 띄었다.

“힘드냐?”

혁무진이 소매로 이마의 땀을 훔치며 대답했다.

“솔직히 힘들긴 한데…… 이상하게 지난번보다는 훨씬 낫네요.”

“지난번이라니?”

“벌써 잊으셨어요? 정찰 임무 때요.”

“아, 기억난다.”

백호당 소속으로 정찰 임무를 맡았다가 조필을 만나는 바람에 죽을 뻔했던 일. 그때도 분명 말을 끌고 가긴 했었지.

‘나중에는 폭설이 내리는 바람에 말도 버리고 갔지만.’

예전 일을 떠올리자 피식 웃음이 새어 나왔다.

“왜 그러세요?”

“네 생각 나서. 나한테 멋모르고 까불다가 엄청 맞았잖아.”

“……꼭 그렇게 지난 얘기를 들춰내야 속이 후련하세요?”

“물어본 건 너야, 인마.”

“어쨌든, 그때보다는 훨씬 나아진 것 같다고요.”

“그래?”

“네. 정찰 임무 때보다 훨씬 많이 달렸는데 별로 지치지도 않고 그러네요. 말 타는 게 좀 익숙해져서 그런가?”

“그런 걸지도…… 아, 잠깐만.”

“예?”

문득 짚이는 구석이 있어 기감을 끌어올렸다.

띠링. 익숙한 시스템 알림과 함께 어리둥절해하는 혁무진의 얼굴 위로 레벨창이 떠오른다.



[Lv.38 혁무진]



“……엥?”

벌어진 입에서 바람 빠지는 소리가 새어 나온다. 혁무진이 언제부터 레벨이 이렇게 높았지?

‘엄밀히 말해서 엄청나게 높은 건 아니지만.’

녀석과 처음 만났을 때 20레벨에 불과했던 걸 생각하면 장족의 발전이라는 말도 부족하다. 이 정도면 거의 새로 태어난 수준인데?

‘그러고 보면 처음 만난 이후로 꾸준히 올랐던 것 같기도 하고.’

기억을 더듬어 보니 처음보다 또렷하게 떠올릴 수 있었다.

정찰조로 재회했을 때도 그랬고, 틈틈이 기감을 끌어올릴 때마다 옆에 있던 혁무진의 레벨은 1, 2씩 올라 있었다.

그러던 게 어느새 38레벨. 무림에서의 시간으로만 치면 근 두 달 남짓한 시간 동안 두 배 가까이 성장을 이룬 거다.

‘그럼 혹시?’

설마 하는 마음에 혁무진을 뚫어져라 바라봤다.

이 녀석도 나처럼 스탯 포인트를 받는다면? 그걸 내가 대신 분배해 줄 수도 있지 않을까?

‘가능성이 있는 이야기지.’

내가 비슷한 레벨의 헌터나 무인보다 훨씬 강한 걸로 봐서는 시스템 보정 효과가 있는 것 같긴 한데…….

‘한 번 시도해 볼 만해.’

“왜 그러세요? 제 얼굴에 뭐라도 묻었습니까?”

“아니. 그냥 못생겨서.”

“……아, 진짜.”

꿍얼거리는 혁무진의 어깨를 잡고 마음으로 외쳤다.

‘상태창 오픈!’

바로 그 순간.

“뭐 하세요? 어깨 아파요.”

“어, 그래.”

아무 일도 없네. 뭐 하나쯤 뜰 줄 알았는데.

하긴 본캐도 만렙 찍으려면 아직 한참 남았는데 부캐가 웬 말이냐. 그래도 아쉽긴 하다.

‘소리 내서 해 볼까?’

분명히 이상한 놈 취급받겠지만 화장실 다녀와서 손 안 닦는 기분으로 가는 것보단 낫겠지.

나는 슬그머니 혁무진의 등에 손을 살짝, 아주 살짝 가져다 대며 작게 중얼거렸다.

“상태창 오픈.”

“아, 진짜. 아까부터 진짜 왜 이러세요?”

녀석의 말을 무시하고 자리에서 벌떡 일어났다.

기다리던 알림 소리와 함께 시스템창이 떴기 때문이었다.

“이야아, 떴다!”

띠링.



- 퀘스트 조건에 [제한 시간]이 추가되었습니다.

- [22:00:00] 안에 항산검문에 도착하십시오. 늦는다면 돌이킬 수 없게 됩니다.



“이야아…….”

사그라지는 목소리. 흔들리는 눈동자.

‘제한 시간이라니. 뭔 놈의 제한 시간.’

나한테 왜 이러냐, 진짜.

한숨을 푹 내쉬는 내게 눈을 동그랗게 뜬 월화가 물었다.

“진 공자, 어디 아파요?”

“아뇨. 그건 아니고요. 혹시 우리 언제쯤 도착하는지 알 수 있어요?”

“음. 오늘 같은 속도라면 내일 저녁 전에?”

“아.”

지금 정오를 약간 넘긴 시간이니까 꼬박 하루는 넘게 달려야 한단 말이다.

퀘스트창이 변경된 걸 보니 그 제한 시간 안에 적풍단 놈들이 항산검문을 친다는 얘기 같은데…… 이걸 어쩐다?

“이제 슬슬 출발할까요?”

“말들이 지쳤어요. 반 시진은 쉬어야 해요.”

“말들아, 괜찮지? 방금 들으셨어요? 괜찮다고 대답한 거.”

“…….”

그래, 그런 눈으로 볼 줄 알았다.
```

## Final English reading copy

```markdown
# Chapter 110

*Bang!*

The person who appeared with the thunderous explosion was a middle-aged man of imposing stature.

Beneath his thick, sharply angled brows, he glared around the room with tiger eyes like an enraged beast.

“Who was the one spouting that nonsense just now?”

Everyone gathered here was a senior figure of the Mount Heng Sword Sect.

Even if they weren’t on their predecessor’s level, they possessed First Rate martial arts and more than enough experience. Yet even they were busy shrinking their necks and avoiding his gaze.

The middle-aged man before them had every right to make them do so.

*Damn it. Of all people, it had to be the Tiger of Mount Heng…*

The storytellers said that two beasts lived on Mount Heng.

The Blood Wolf Sword and the Tiger of Mount Heng. They were close friends, but each was also the wall the other had to overcome.

The middle-aged man, Cheol Mubaek, had been a Peak master known as the tiger of Mount Heng for decades.

“I asked which one of you it was!”

At that roar, the senior figures of the Mount Heng Sword Sect felt every hair on their bodies stand on end.

They said that whenever Cheol Mubaek lost his temper, even his friend Lee Cheonbaek would leave the area. These men were far inferior to him in both martial arts and age, so there was no need to say more.

“We should be united in driving out those mounted bandit bastards, and yet you dare defy Cheonbaek’s final wishes and harbor rebellious intentions?”

Under his gaze, which seemed ready to pour out flames, the senior figures of the Mount Heng Sword Sect flinched as though they had been burned.

“G-Great Hero Cheol. You misunderstand.”

“How could we ever dare harbor rebellious intentions?”

“Then have I grown old enough for my ears to fail me?”

At that moment, everyone inside the main hall felt thirsty. It wasn’t a simple illusion. It was caused by the terrifying Scorching Yang Qi radiating from Cheol Mubaek.

*What the hell?*

*What on earth has he been eating to build up such ridiculous internal energy…?*

Just being near him made it hard to breathe, and sweat poured down their bodies. The Tiger of Mount Heng. This was the moment the true nature of the Peak master who had supposedly trained alone somewhere in the vast mountain range since around the age of twenty revealed itself.

“Haah… Hoo…”

“Great Hero, please calm down… Hah.”

The senior figures of the Mount Heng Sword Sect panted harshly, while the Peak master glared at them without the slightest sign of forgiveness.

The air inside the main hall was about to boil like lava when—

“Uncle Cheol, it’s hot.”

A clear voice like a flowing stream, and slender white fingers tugging at Cheol Mubaek’s sleeve. At the same time, the wrinkles furrowed across his brow in anger smoothed out as though someone had pulled them flat.

“W-Was it very hot?”

“Yes. I can barely breathe.”

“Goodness, I didn’t think of you. How are you now?”

“Much better. Thank you, Uncle Cheol.”

“Don’t say such things. Protecting you, Seowol, is my duty.”

Cheol Mubaek’s powerful Scorching Yang Qi subsided.

Only then did the people throughout the hall finally release the breaths they had been holding. Once they came to their senses, their clothes drenched in sweat, they realized that Cheol Mubaek was not alone.

“Y-Young Lady.”

“We greet Young Lady.”

Cheol Mubaek raised his brows at the senior figures hurriedly standing to show their respect. But the “Young Lady” was faster.

“I’ll tell the two of you one last time, Iron Sword Squad Leader and Master of the Gatekeeper Pavilion.”

The woman who had been hidden behind Cheol Mubaek’s massive frame stepped forward. She was slim and graceful, and the hem of her blue gown rustled whenever it brushed the floor.

“Change how you address me. Not Young Lady. Sect Leader.”

Those who met her frost-cold gaze remembered one fact they had momentarily forgotten.

*Oh. That’s right.*

The Blood Wolf Sword, Lee Cheonbaek.

Lee Seowol was the child in whom his blood ran strongest.

* * *

I knew nothing about horseback riding. After coming to Murim, I had ridden only a few times. In the modern world, horseback riding was practically an aristocratic sport reserved for the rich, so I’d never had the chance to try it.

But perhaps because my physical abilities were so good and I was riding a well-trained horse, I had enough leisure to look at the System Window even during a furious gallop.

*Open Quest Window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally you must join hands with. Invite them to the Jin Family of Taiyuan during the upcoming Lunar New Year.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

Quests were fluid. Sometimes sudden Quests appeared depending on the situation, and sometimes, like now, an existing Quest was updated.

*The Grade was raised.*

The Quest Grade changing from First Rate to Peak meant that the road to the Mount Heng Sword Sect had become anything but easy.

For example, the Red Wind Band. Or the Red Wind Band. Probably the Red Wind Band…

Never mind. Thinking about it any more would only hurt.

*Every day in this place is a walk across thin ice.*

I thought I’d finally received an easy Quest for once, but trouble had struck again.

The reason I wasn’t as anxious as before was partly because of the reliable presence of Jin Mukyung, but also because I myself had grown stronger.

*Open Status Window.*

*Ding.*

> **System**
>
> **Status Window**
>
> **Level:** 55 — Jin Taekyung
>
> **Class:** First Rate martial artist
>
> **Fame:** 1,300 (+150)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +10, Fame +100)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+25)  
> **Stamina:** 195 (+25)
>
> **Agility:** 192 (+25)  
> **Intelligence:** 35 (+25)
>
> **Charm:** 35 (+25)  
> **Internal energy:** 15 years
>
> **Toughness:** 155 (+25)
>
> **Remaining Points:** 0

*Ahh, barkeep.*

*Look how well I’ve grown. All by myself.*

Strength, Agility, and Stamina were each nearing 200. Just looking at them made me feel full, and my Toughness, born from getting beaten by Jin Mukyung, was growing nicely too.

*The Title bonuses are hefty, too. This should be enough.*

Until now, I had raised my stats just to survive. Every time I advanced a Quest, one crisis after another came crashing down like three waves at once. There was no way I could afford to invest points in Charm or Intelligence.

*Even if I raised my Intelligence enough to reach an IQ of 180, it’s not like I’d start thrusting a spear scientifically.*

Charm was the same. It wasn’t as though Jopil or the Head Elder would spare me just because I was handsome.

Of course, raising them would help me in some way eventually. But with my life hanging by a thread, I hadn’t had the courage to invest in noncombat stats.

*I can protect this one life of mine to some extent now.*

Once this Quest was over, I planned to pay more attention to my internal energy and noncombat stats.

As it happened, the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory.

*Of course, if I screw up taking it, I could wind up dead.*

At that moment, Wolhwa, who had been riding at the front, spotted a stream and stopped.

“We’ll rest for a little while. The horses are too exhausted.”

How much time had passed?

We had ridden without stopping since leaving the shrine; dawn had broken, and now the sun was high overhead. System messages saying my Strength and Stamina had increased had even appeared twice, so it had definitely been a forced march.

“Whew. My butt hurts like hell. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.”

While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious.

“Is it hard?”

Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering.

“To be honest, it is… But strangely, it’s much better than last time.”

“Last time?”

“You’ve already forgotten? During the scouting mission.”

“Ah, I remember.”

I had nearly died after encountering Jopil while carrying out a scouting mission for White Tiger Hall. We’d taken horses with us then, too.

*Though we ended up abandoning them when the heavy snow came.*

Remembering the past, I let out a quiet laugh.

“What’s wrong?”

“I was thinking about you. You mouthed off to me without knowing what you were doing and got the crap beaten out of you.”

“……Do you really have to dredge up the past to feel better?”

“You’re the one who asked, punk.”

“Anyway, I’m saying it seems much better than back then.”

“Really?”

“Yes. We’ve ridden much farther than during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?”

“Maybe… Ah, wait.”

“Hm?”

Something suddenly occurred to me, so I heightened my Qi Sense.

*Ding.*

Along with a familiar system notification, a Level Window appeared over Hyuk Mujin’s bewildered face.

> **System**
>
> **Level:** 38 — Hyuk Mujin

“……Huh?”

A breathy sound escaped his open mouth. When had Hyuk Mujin’s Level gotten this high?

*Strictly speaking, it wasn’t all that high.*

But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn.

*Come to think of it, his Level did seem to keep rising after we first met.*

As I searched my memory, the details came back more clearly.

It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two.

And now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in only about two months.

*Then maybe…?*

With a doubtful heart, I stared intently at Hyuk Mujin.

What if he received stat points like I did? Could I distribute them for him?

*It’s possible.*

Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect…

*It’s worth trying once.*

“Why are you looking at me like that? Do I have something on my face?”

“No. You’re just ugly.”

“……Seriously.”

I grabbed Hyuk Mujin’s shoulder and shouted inwardly.

*Open Status Window!*

At that very moment—

“What are you doing? My shoulder hurts.”

“Oh. Okay.”

Nothing happened. I thought at least something would appear.

Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing.

*Should I say it out loud?*

They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom.

I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath.

“Open Status Window.”

“Seriously. What is wrong with you today?”

Ignoring him, I sprang to my feet.

The system window had appeared with the notification chime I’d been waiting for.

“Yes! There it is!”

*Ding.*

> **System**
>
> The Quest condition **Time Limit** has been added.
>
> Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no going back.

“Yes…”

My voice faded. My eyes began to tremble.

*A time limit? What kind of time limit is this?*

*Why are you doing this to me?*

As I let out a deep sigh, Wolhwa’s eyes widened and she asked,

“Young Master Jin, are you hurt?”

“No, it’s not that. Do you know around when we’ll arrive?”

“Hmm. At today’s pace, before tomorrow evening?”

“Ah.”

It was a little past noon now. That meant we would have to ride for more than an entire day.

Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit…

What was I supposed to do?

“Shall we get going soon?”

“The horses are tired. We need to rest for an hour.”

“Horses, you’re all right, aren’t you? You heard that, right? They said they’re fine.”

“……”

Yeah. I knew you’d look at me like that.
```
